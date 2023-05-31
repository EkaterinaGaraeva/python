# Задача 40: Работать с файлом california_housing_train.csv,
# который находится в папке sample_data.
# Определить среднюю стоимость дома, где кол-во людей от 0 до 500 (population).


import pandas as pd

df = pd.read_csv("california_housing_train.csv")


df1 = df.loc[df.population <= 500]
print(round(df1.median_house_value.mean(), 4))
print(df1.median_house_value.median())


print(round(df.loc[(df.population <= 500), ['median_house_value']].mean(), 4))
print(df.loc[(df.population <= 500), ['median_house_value']].median())

