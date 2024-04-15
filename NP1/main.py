import numpy as np

dataset = np.loadtxt('brands.csv', delimiter=";", dtype=str, encoding="utf-8")


# Q1
brands = dataset[1:, 0].copy() # Slicing brand column
values_2021 = dataset[1:, 10].astype(float).copy() # Slicing values of 2021 column
values_2022 = dataset[1:, 9].astype(float).copy() # Slicing values of 2022 column

cond = brands=="Google" # conditional to search for Google data
value_google_2021 = values_2021[cond][0] # getting value of 2021
value_google_2022 = values_2022[cond][0] # getting value of 2022
print(f"Q1 - Valorização do Google de 2021 para 2022: {value_google_2022 - value_google_2021}")


# Q2
cond = np.char.find(brands, "Group")>=0 # Conditional to find "Group" substring
print(f"\nQ2 - Quantidade de marcas com a palavra group no nome: {len(brands[cond])}")


# Q3
five_brands = brands[:5] # Slicing the five firsts brands
five_values_2022 = values_2022[:5] # Slicing the five first values of 2022
five_values_2023 = five_values_2022 * 1.1 # Calc the possible value of 2023
print("\nQ3 - Possível valor das 5 primeiras marcas em 2023 ($M)")
for i in range(0,5): # Printing
    print(f"{five_brands[i]} : {round(five_values_2023[i], 2)}")
    
    
# Q4
# OBS: I also have brands sliced
founded_by = dataset[1:, 1] # Slicing founded_by column
founded_year = dataset[1:, 2].astype(int) # Slicing founded_in column
cond = founded_year > 2000 # Cond to search for brands founded after 2000
print(f"\nQ4- Marcas fundadas após 2000: {brands[cond]}")


# Q5
unique_years, frequency_years = np.unique(founded_year, return_counts=True) # Getting unique values and their frequency
most_year = np.argmax(frequency_years) # Getting the index of the biggest value in frequency_years
print(f"\nQ5 - Ano com mais empresas fundadas: {unique_years[most_year]}")