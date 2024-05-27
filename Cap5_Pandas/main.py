import numpy as np
import pandas as pd

# SERIES
dic = {
    'a': 10,
    'b': 20,
    'c': 30
}
s1 = pd.Series(dic)
s2 = pd.Series(data=[20,30,40], index=['b','c','d'])
print(s1.add(s2, fill_value=0))
print(s1['a'])
print(s1[['b', 'c']])
print(s1[s1>10])


# DATAFRAME
df = pd.DataFrame(
    columns=['X', 'Y', 'Z'],
    index=['A', 'B', 'C'],
    data=np.random.randint(1, 50, [3,3])
)

# slicing (2 ways to do the samething)
print(df.loc[['B','C'], ['X','Y','Z']])
print(df.iloc[1:, :])

# lendo
df = pd.read_csv('./Datasets/paises.csv', delimiter=';')
print(df.columns)
print(df['Country'])
print(df.head(3))
print(df.tail(3))
