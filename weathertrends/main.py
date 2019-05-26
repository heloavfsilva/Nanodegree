import pandas as pd
import matplotlib.pyplot as plt
from numpy import NaN
from datetime import datetime

# Import the files to be used
city_data = pd.read_csv("city_data.csv", index_col=["year"])
#print(city_data.head())

city_list = pd.read_csv("city_list.csv")
#print(city_list.head())

global_data = pd.read_csv("global_data.csv")
# print(global_data.head())

#Filter the Brazil cities list
isBrazil = city_list['country'] == 'Brazil'
city_list_br = city_list[isBrazil]

# Filter the all city data in Brazil
city_data_br = city_data['city']== 'Belo Horizonte'
city_data_br = city_data[city_data_br]
# print(city_data_br.head())
# city_br_mva = pd.Series(city_data_br)

year = 3
mva_global = global_data
mva_global = mva_global.replace(0, NaN)
mva_global = mva_global.dropna(how='all', axis=0)
mva_global = global_data.rolling(year).mean()
# print(mva_global)

mva_local = city_data_br.drop(['city', 'country'], axis=1)
mva_local = mva_local.replace(0, NaN)
mva_local = mva_local.dropna(how='all', axis=0)
mva_local = mva_local.rolling(year).mean()

# print(mva_local);

df = pd.merge(mva_local, mva_global, on='year')
print(df)

fig = plt.figure()
plt.plot('year', 'avg_temp_x', data=df, marker='', color='skyblue', linewidth=2, label="Local")
plt.plot('year', 'avg_temp_y', data=df, marker='', color='olive', linewidth=2, linestyle='dashed', label="Global")

plt.xlabel('year', fontsize=18)
plt.ylabel('degree', fontsize=16)
plt.title('Weather trends for Belo Horizonte in '+str(year)+' years avg')
fig.savefig('BH-'+str(year)+'years.png')
plt.show()


