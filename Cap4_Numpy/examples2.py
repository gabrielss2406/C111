import numpy as np

# NUMEROS ALEATORIOS
np.random.seed(10)
arr = np.random.randint(1, 11, 15) # 15 numeros de 1 a 10 (high exclusivo)
print(arr)

# EXTRAINDO ELEMENTOS UNICOS
print(np.unique(arr, return_counts=True))

# OPERAÇÕES EM MATRIZES
mtz = arr.reshape(3, 5)
print(mtz)
print(mtz.sum(axis=1)[0])
print(mtz.sum(axis=0)[0])

# BROADCASTING
print(0.5*mtz)

# CONDICIONAIS
print(mtz[mtz%2==0])
print(mtz[mtz>mtz.mean()])

# ANALISE TEXTUAL
# CHAR
arr = np.array(["Junior Santos", "Savarino", "Tiquinho", "A. Barboza"])
result = np.char.find(arr, 'a')
print(result[result>=0])