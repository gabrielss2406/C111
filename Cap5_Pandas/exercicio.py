import numpy as np
import pandas as pd

df = pd.read_csv('./Datasets/paises.csv', delimiter=';')

# 1
oceania_df = df[df['Region'].str.contains('OCEANIA')]
print(f"Países da Oceania: {oceania_df}") # a
print(f"Quantidade da países da Oceania: {oceania_df.shape[0]}") # b


# 2
print("================================")
mean_literacy = df["Literacy (%)"].mean()
print(f"Média de alfabetização no planeta {round(mean_literacy,2)} %")


# 3
print("================================")
max_population = df["Population"].max()
country_population = df[df["Population"] == max_population]
print(f"País: {country_population.iloc[0]["Country"]}\nPopulação: {max_population} pessoas")


# 4
print("================================")
whitout_coast_country_names = df[df["Coastline (coast/area ratio)"] == 0]["Country"]
whitout_coast_country_names.to_csv("./Cap5_Pandas/noCoast.csv", sep=";", header=False, index=False)
print("Nome dos países sem costa salvos em um novo .csv")
