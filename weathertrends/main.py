import pandas as pd
import matplotlib.pyplot as plt
from numpy import NaN

# Import the files to be used
city_data = pd.read_csv("city_data.csv", parse_dates=["year"], index_col=["year"])
#print(city_data.head())

city_list = pd.read_csv("city_list.csv")
#print(city_list.head())

global_data = pd.read_csv("global_data.csv")
#print(global_data.head())

#Filter the Brazil cities list
isBrazil = city_list['country'] == 'Brazil'
city_list_br = city_list[isBrazil]

# Filter the all city data in Brazil
city_data_br = city_data['city']== 'Belo Horizonte'
city_data_br = city_data[city_data_br]
#print(city_data_br.head())

#city_br_mva = pd.Series(city_data_br)

mva = city_data_br.drop(['city', 'country'], axis=1)
mva= mva.replace(0, NaN)
mva=mva.dropna(how='all', axis=0)
mva7 = mva.rolling(7).mean()
mva5 = mva.rolling(5).mean()
mva2 = mva.rolling(2).mean()

# print(mva)
fig = plt.figure()
plt.plot(mva2)
plt.xlabel('year', fontsize=18)
plt.ylabel('degree', fontsize=16)
plt.title('Weather trends for Belo Horizonte in 2 years avg')
fig.savefig('BH-2years.jpg')
plt.show()


