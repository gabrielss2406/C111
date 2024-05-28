import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# PLOT SIMPLES
x = np.array([1, 2, 3, 4])
y = x*2 # broadcasting
y2 = x**2
# plot
plt.xlabel("Valores de x")
plt.ylabel("Valores de y")
plt.plot(x, y, 'o--g', # grafico 1
         x, y2, 'x:b', # grafico 2
         linewidth=2, markersize=10)
plt.show()


# SUBPLOT 1
plt.subplot(1, 2, 1)
plt.plot(x, y, 'o-r')
plt.title('Linear')
# SUBPLOT 2
plt.subplot(1, 2, 2)
plt.plot(x, y2, 'x--g')
plt.title('Exponencial')

plt.show()