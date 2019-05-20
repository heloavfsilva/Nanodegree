import pandas as pd
import matplotlib.pyplot as plt

# Import the files to be used
from numpy import NaN

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
mva = mva.rolling(5).mean()

print(mva)
plt.plot(mva)

plt.show()