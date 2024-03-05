import numpy as np

# Operações entre numpy arrays
jan = np.arange(20, 30, 1)
fev = np.arange(40, 50, 1)
print(jan)
print(fev)
print(jan+fev)
print(np.concatenate([jan, fev])).reshape(5, 4)

# Tamanho de um ndarray
print(jan.size)
# Dimensão de um ndarray
print(jan.ndim)
# Shape de um ndarray
print(jan.shape)