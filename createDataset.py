# %%
import json
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


df1 = pd.read_csv('allanturn/allanturnParsed.csv', index_col=0)
df2 = pd.read_csv('pensacolaCarDealers/PensacolaCarDealers.csv', index_col=0)
df3 = pd.read_csv('hillkelly/hillkelly.csv', index_col=0)
df4 = pd.read_csv('cardeals/cardeals.csv', index_col=0)
df5 = pd.read_csv('sandysansing/sandySansing.csv', index_col=0)
df6 = pd.read_csv('allstar/allstar.csv', index_col=0)
df7 = pd.read_csv('petemoore/petemoore.csv', index_col=0)
df8 = pd.read_csv('downtownMotors/downtownMotors.csv', index_col=0)
df9 = pd.read_csv('mckenziemotors/mckenziemotors.csv', index_col=0)

with open('consumerReports.json') as file:
    carIDs = json.load(file)['response']

df = pd.concat([df1, df2, df3, df4, df5, df6, df7, df8, df9])
df = df.reset_index(drop=True)
df.to_csv('PensacolaCarDataset.csv')

# %%

df['modelYearId'] = 0

for (i, car) in df.iterrows():
    try:
        make = car['Manufacturer'].lower()
        for gtMake in carIDs:
            if gtMake['makeName'].lower() == make:
                model = car['Model'].lower()
                for gtModel in gtMake['models']:
                    if gtModel['modelName'].lower() == model:
                        year = car['Year']
                        for gtYear in gtModel['modelYears']:
                            if gtYear['modelYear'] == year:
                                # print(gtMake['makeName'], make, gtModel['modelName'], model, year)
                                df.loc[i, 'modelYearId'] = gtYear['modelYearId']
    except:
        pass

(df['modelYearId'] != 0).mean()
#%%
df.to_csv('PensacolaCarDataset.csv')
#%%
with open('carStyles.json') as file:
    carStyles = json.load(file)

with open('carValues.json') as file:
    carValues = json.load(file)
# %% All types of vehicles
df['MarketValue'] = float('nan')

for (i, car) in df.iterrows():
    modelId = car['modelYearId']
    if str(modelId) in carStyles:
        styles = carStyles[str(modelId)]
        priceSum = 0
        priceN = 0
        for style in styles:
            priceSum += carValues[str(style)]
            priceN += 1
        if priceN > 0:
            df.loc[i, 'MarketValue'] = priceSum / priceN
# %%
df.to_csv('PensacolaCarDataset.csv')
# %%
