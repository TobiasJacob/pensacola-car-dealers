#%%
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('PensacolaCarDataset2021-10-05.csv', index_col=0)
dfOld = pd.read_csv('PensacolaCarDataset2020-09-28.csv', index_col=0)
#%%
print('Before:')
dealers = df['Dealer'].unique()
before = {}
for d in dealers:
    count = (df['Dealer'] == d).sum()
    print(d, count)
    before[d] = count

#%%

df = df[df['Price'].apply(lambda x: type(x) in [float, int] or x.isnumeric())]
df['Price'] = df['Price'].astype(float)
df = df[df['Price'] != 0]
df = df[df['Mileage'] != 0]

df.to_csv('PensacolaCarDataset.csv')
# %%
print('After clean:')
dealers = df['Dealer'].unique()
for d in dealers:
    print(d, before[d], '->', (df['Dealer'] == d).sum())
df.dtypes

# %% Dealer Places
dealers = df['Dealer'].unique().tolist()
rgb_values = sns.color_palette("Set2", len(dealers))
color_map = dict(zip(dealers, rgb_values))

fig, ax = plt.subplots(1)
for (i, d) in enumerate(dealers):
    df[df['Dealer'] == d].plot.scatter('Year', 'Mileage', 3, ax=ax, c=color_map[d], label=d)
ax.legend(loc='upper right')

# %% Dealer Mean Positioning
dealers = df['Dealer'].unique().tolist()
rgb_values = sns.color_palette("Set2", len(dealers))
color_map = dict(zip(dealers, rgb_values))
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 8))

for (i, d) in enumerate(dealers):
    df[df['Dealer'] == d].plot.scatter('Mileage', 'Year', 3, ax=ax2, c=color_map[d], label=d)
ax.legend(loc='upper right')

for (i, d) in enumerate(dealers):
    data = df[df['Dealer'] == d]
    ax1.scatter(data['Mileage'].mean(), data['Year'].mean(), 3, c=color_map[d], label=d)
ax1.legend(loc='upper right')
ax2.legend(loc='upper right')
ax1.set_xlabel('Mileage')
ax1.set_ylabel('Year')
ax1.set_xlim(ax2.get_xlim())
ax1.set_ylim(ax2.get_ylim())


# %% Dealer Mean Pricing (Miles)
dealers = df['Dealer'].unique().tolist()
rgb_values = sns.color_palette("Set2", len(dealers))
color_map = dict(zip(dealers, rgb_values))
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 8))


for (i, d) in enumerate(dealers):
    df[df['Dealer'] == d].plot.scatter('Mileage', 'Price', 3, ax=ax2, c=color_map[d], label=d)
ax.legend(loc='upper right')

for (i, d) in enumerate(dealers):
    data = df[df['Dealer'] == d]
    ax1.scatter(data['Mileage'].mean(), data['Price'].mean(), 3, c=color_map[d], label=d)
ax1.legend(loc='upper right')
ax2.legend(loc='upper right')
ax1.set_xlabel('Mileage')
ax1.set_ylabel('Price')
ax1.set_xlim(ax2.get_xlim())
ax1.set_ylim(ax2.get_ylim())

# %% Dealer Mean Pricing (Year)
dealers = df['Dealer'].unique().tolist()
rgb_values = sns.color_palette("Set2", len(dealers))
color_map = dict(zip(dealers, rgb_values))
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 8))


for (i, d) in enumerate(dealers):
    df[df['Dealer'] == d].plot.scatter('Year', 'Price', 3, ax=ax2, c=color_map[d], label=d)
ax.legend(loc='upper right')

for (i, d) in enumerate(dealers):
    data = df[df['Dealer'] == d]
    ax1.scatter(data['Year'].mean(), data['Price'].mean(), 3, c=color_map[d], label=d)
ax1.legend(loc='upper right')
ax2.legend(loc='upper right')
ax1.set_xlabel('Year')
ax1.set_ylabel('Price')
ax1.set_xlim(ax2.get_xlim())
ax1.set_ylim(ax2.get_ylim())

# %% Average Price per Year

fig, ax1 = plt.subplots()
values = df.groupby('Year').mean()
values['Mileage'].plot(ax=ax1)
ax1.set_ylabel('Mileage')
ax1.legend(['Mileage'], loc='upper left')

ax2 = ax1.twinx() 
values['Price'].plot(ax=ax2, c='orange')
ax2.set_ylabel('Price')
ax2.legend(['Price'], loc='upper right')
# %% Average Price per Mile

fig, ax1 = plt.subplots()
values = df.copy()
values['Mileage'] = 5000 * (values['Mileage'] // 5000)
values = values.groupby('Mileage').mean()

values['Year'].plot(ax=ax1)
ax1.set_ylabel('Year')
ax1.legend(['Year'], loc='upper left')

ax2 = ax1.twinx() 
values['Price'].plot(ax=ax2, c='orange')
ax2.set_ylabel('Price')
ax2.legend(['Price'], loc='upper right')

# %% Dealer Prices Detail
dealers = df['Dealer'].unique().tolist()
rgb_values = sns.color_palette("Set2", len(dealers))
color_map = dict(zip(dealers, rgb_values))

fig, ax = plt.subplots(1, figsize=(10, 10))
for (i, d) in enumerate(dealers):
    df[df['Dealer'] == d].plot.scatter('Mileage', 'Price', 20, ax=ax, c=color_map[d], label=d)
plt.gca().set_ylim([0, 20000])
plt.gca().set_xlim([0, 180000])
ax.legend(loc='upper right')

# %%
dealers = df['Dealer'].unique().tolist()
rgb_values = sns.color_palette("Set2", len(dealers))
color_map = dict(zip(dealers, rgb_values))
fig, ax = plt.subplots(1, figsize=(10, 10))
for (i, d) in enumerate(dealers):
    df[df['Dealer'] == d].plot.scatter('Year', 'Price', 20, ax=ax, c=color_map[d], label=d)
plt.gca().set_ylim([0, 20000])

# %%

dealers = [d for (d, c) in df['Manufacturer'].value_counts().iteritems() if c > 75]
rgb_values = sns.color_palette("Set2", len(dealers))
color_map = dict(zip(dealers, rgb_values))
fig, ax = plt.subplots(1, figsize=(20, 20))
for (i, d) in enumerate(dealers):
    df[df['Manufacturer'] == d].plot.scatter('Mileage', 'Price', ax=ax, c=color_map[d], label=d)

# %%
df.query("Mileage < 120000 & Year > 2010 & Price < 10000 & Dealer != 'Car Deals' & Dealer != 'All star'").sort_values('Price')

# %%
dealers = df['Dealer'].unique()
rgb_values = sns.color_palette("Set2", dealers.size)
color_map = dict(zip(dealers, rgb_values))
fig, ax = plt.subplots(1)
for i in range(dealers.size):
    plotData = df[df['Dealer'] == d]
    plotData = plotData[plotData.Manufacturer.str.contains('NISSAN')]
    if len(plotData.index) > 0:
        plotData.plot.scatter('Mileage', 'Price', 3, ax=ax, c=color_map[d], label=d)
plt.gca().set_ylim([0, 30000])

# %%

df.hist('Mileage', bins=100)
plt.gca().set_xlim([0, 180000])
# %%
dealer = df['Dealer'].unique()
fig, ax = plt.subplots(1)
plt.hist([df[df.Dealer == d]['Mileage'] for d in dealer], stacked=True, bins=100)
plt.legend(dealer)
plt.gca().set_xlim([0, 180000])
# %%

plt.hist([df['Price'] - df['MarketValue']], bins=50)
# %%
df['Overprice'] = df['Price'] - df['MarketValue']
df['RelOverprice'] = df['Overprice'] / df['Price']
# %%
df.query("Mileage < 120000 & Year > 2010 & Price < 10000 & Dealer != 'Car Deals' & Dealer != 'All star'").sort_values('RelOverprice')
# %%
df[df['Price'] < 10000].sort_values('RelOverprice').head(1000)
# %%
dfRelevant = df
y = dfRelevant.groupby('Dealer').RelOverprice.mean().mean()
plt.plot([0, 6], [y, y], c='red')
dfRelevant.groupby('Dealer').RelOverprice.mean().plot.bar()
# %%
dfRelevant = df[df.Price < 10000]
y = dfRelevant.groupby('Dealer').RelOverprice.mean().mean()
plt.plot([0, 6], [y, y], c='red')
dfRelevant.groupby('Dealer').RelOverprice.mean().plot.bar()
# %%
dfNew = df[[i not in dfOld.index for i in df.index]]
dfNew.query('Price < 6000').sort_values('Price')
# %%
dfSold = dfOld[[i not in df.index for i in dfOld.index]]
dfNotSold = dfOld[[i in df.index for i in dfOld.index]]
dfSold.shape[0], dfNotSold.shape[0]
# %%

ax = dfSold.plot.scatter('Price', 'Mileage')
dfNotSold.plot.scatter('Price', 'Mileage', color='red', ax=ax)

# %%
dfSold.Price.mean(), dfNotSold.Price.mean()
# %%
