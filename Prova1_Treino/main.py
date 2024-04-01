import numpy as np

dataset = np.loadtxt('./Prova1_Treino/paises.csv', delimiter=';', dtype=str, encoding='utf-8')

# 1. Faça um slicing no dataset pegando certas colunas
sliced = dataset[1:, :4]
print(sliced[:10])

# 2. Conte e mostre diferentes regioes
regions = np.unique(sliced[1: , 1])
print(len(regions))

# 3. Mostre media da alfabetizacao
literacy = dataset[1:, 9].astype(float)
print(f'{round(np.mean(literacy), 2)} %')

# 4. Conte quantos países são da América do Norte
count_regions = sliced[1: , 1]
count_regions = count_regions[np.char.find(count_regions, "NORTHERN AMERICA")>=0]
print(f"{len(count_regions)} países da América do Norte.")

# 5. Encontre qual país da América do Sul e Caribe com maior renda
countries = sliced[:, 0]
regions = sliced[:, 1]
gdp = dataset[1:, 8].astype(float)
cond = np.char.find(regions, "LATIN AMER. & CARIB")>=0

best_country = np.argmax(gdp[cond])
countries = countries[cond]
print(f"{countries[best_country]}")