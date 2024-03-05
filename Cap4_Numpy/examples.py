import numpy as np

# NumPy Array
# 1-D
arr = np.array([1, 2, 3, 4])
print(type(arr))

# 2-D
mtz = np.array([[1, 2], [3, 4]])
print(mtz)

# 3-D
arr = np.zeros(10)
print(arr)

# arange
arr = np.arange(20, 30, 1)
print(arr)

# reshape
arr = arr.reshape(5, 2)
print(arr)