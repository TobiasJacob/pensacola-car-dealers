#%%
import pandas as pd 

df1 = pd.read_csv('originalDataset/PensacolaCarDataset2020-09-28.csv')
df2 = pd.read_csv('originalDataset/PensacolaCarDataset2020-10-11.csv')

# %%
df1 = df1.set_index('VIN')
df2 = df2.set_index('VIN')
df1 = df1.drop('Unnamed: 0',axis = 1)
df2 = df2.drop('Unnamed: 0',axis = 1)

#%%
df1.Price = df1.Price.apply(lambda v: str(int(float(v))))
df1.Manufacturer = df1.Manufacturer.apply(lambda m: m[0].upper() + m[1:].lower())
df2.Manufacturer = df2.Manufacturer.apply(lambda m: m[0].upper() + m[1:].lower())



# %%
for (index, car) in df1.iterrows():
    if index not in df2.index:
        # print('Sold car ', car['Manufacturer'], car['Model'], car['Price'])
        pass
    elif index in df1.index:
        try: 
            if not all(df1.loc[index].eq(df2.loc[index]).drop('Price').drop('MarketValue').drop('Mileage')):
                print('Uneqals ', df1.loc[index], df2.loc[index])
                if car.Dealer == 'Pete Moore':
                    df1.loc[index, 'Model'] = df2.loc[index, 'Model']
        except:
            pass

# %%
for (index, car) in df2.iterrows():
    if index not in df1.index:
        print(index)
# %%
df1 = df1.rename(columns={'Manufacturer': 'Make'})
df2 = df2.rename(columns={'Manufacturer': 'Make'})
df1.to_csv('PensacolaCarDataset2020-09-28.csv')
df2.to_csv('PensacolaCarDataset2020-10-11.csv')
# %%

# %%
