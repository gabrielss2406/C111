import numpy as np

# 1. Crie um array de float com 10 elementos positivos e negativos entre 0 e 1
# Multiplique valores por 100 e crie um novo vetor com a parte inteira
np.random.seed(5)
arr = np.random.randn(10)
arr = arr*100
new_arr = arr[arr>=0]
print(f"Novo vetor com a parte inteira {new_arr}")

# 2. Crie matriz 4x4 de inteiros entre 1 e 50
np.random.seed(10)
mtz = np.random.randint(1, 51, 16).reshape(4, 4)
print(f"Matriz 4x4 de 1 a 50:\n{mtz}")


# 3. Mostre a média de cada linha e coluna da matriz anterior
# Aprensentar o maior valor das médias para as linhas e para as colunas
mean_lines = np.mean(mtz, axis=1)
mean_columns = np.mean(mtz, axis=0)
print(f"\nMédia das linhas: {mean_lines}")
print(f"Média das colunas: {mean_columns}")
print(f"Maior média das linhas: {np.max(mean_lines)}")
print(f"Maior média das colunas: {np.max(mean_columns)}")


# 4. Usando matriz da questão 2, mostre aparições de cada número na mesma
# Mostre apenas os que aparecem duas vezes
values, count = np.unique(mtz, return_counts=True)
print(f"Valores que aparecem duas vezes: {values[count==2]}")