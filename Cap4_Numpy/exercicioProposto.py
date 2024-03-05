import numpy as np
import random


# 1 - Array de tamanho 21 com valores linearmente espaçados entre 0 e 1
arr = np.linspace(0 ,1, 21)
print(f"Questão 1: {arr}")

# 2 - Dois arrays
# arr_1 : pares de 0 até 51
# arr_2 : pares de 100 até 50
# arr  : concatene os dois arrays e mostre os resultados ordenados
arr_1 = np.arange(0, 51, 2)
arr_2 = np.arange(100, 50, -2)
arr = np.concatenate([arr_1, arr_2])
arr = np.sort(arr)
print(f"Questão 2: {arr}")

# 3 - Ordenar a questão 2 em ordem descrescente
arr = np.flip(arr)
print(f"Questão 3: {arr}")

# 4 - Matriz formando por 1's de tamanho 3x4. Depois transforme em um array 1-D
mtz = np.ones((3, 4))
mtz = mtz.reshape(-1)
print(f"Questão 4: {mtz}")

# 5 - Crie uma matriz de tamanho qualquer
# Extraia numero de linhas e colunas e multiplique-os
# Diga se esta matriz seria um vetor com numeros par ou impar de elementos
linhas = random.randint(1, 10)
colunas = random.randint(1, 10)
mtz_random = np.random.randint(1, 10, (linhas, colunas))

linhas, colunas = mtz_random.shape
total_elementos = linhas * colunas

print(f"Questão 5: Poderia ser um vetor com numero {'par' if total_elementos % 2 == 0 else 'ímpar'} de elementos.")