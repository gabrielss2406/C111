import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# SCATTER PLOT
df = pd.read_csv('./Datasets/paises.csv', delimiter=';')

df2 = df.nlargest(6, "Area (sq. mi.)") # 6 amiores em area
plt.scatter(x=df2['Country'],
            y=df2['Area (sq. mi.)'],
            s=df2['GDP ($ per capita)']/30)
plt.show()