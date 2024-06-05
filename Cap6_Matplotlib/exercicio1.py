#import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('./Datasets/space.csv', delimiter=';')

companies_eua = df[df["Location"].str.contains("USA")]["Company Name"].unique()
companies_china = df[df["Location"].str.contains("China")]["Company Name"].unique()

countries = ["EUA", "China"]
countries_data = [len(companies_eua), len(companies_china)]

plt.bar(countries, countries_data, color=['blue', 'red'])
plt.xlabel('País')
plt.ylabel('Número de Empresas Espaciais')
plt.title('Número de Empresas Espaciais nos EUA e na China')
plt.show()