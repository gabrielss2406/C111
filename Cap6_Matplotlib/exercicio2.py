#import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('./Datasets/paises.csv', delimiter=';')

north_america_data = df[df['Region'].str.contains("NORTHERN AMERICA")]


plt.plot(north_america_data["Country"], north_america_data["Deathrate"], label='Taxa de Mortalidade', marker='o')
plt.plot(north_america_data["Country"], north_america_data["Birthrate"], label='Taxa de Natalidade', marker='o')

plt.xlabel('Países')
plt.ylabel('Taxas')
plt.title('Taxa de Mortalidade e Natalidade nos Países da América do Norte')
plt.legend(loc='upper right')
plt.grid(True)

plt.tight_layout()
plt.show()
