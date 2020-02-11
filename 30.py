# 30. Wynegeruj listę 1000 liczb losowych o rozkładzie normalnym. Wykreśl histogram oraz średnią, medianę, dominantę, odchylenie standardowe, wariancję, skośność i kurtozę

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

srednia = 0
odchylenie = 1

dane = np.random.normal(srednia, odchylenie, 1000)

plt.hist(dane, 30, density=True)
plt.show()

print("Srednia danych wejsciowych wynosi: {}".format(np.average(dane)))
print("Mediana danych wejsciowych wynosi: {}".format(np.median(dane)))
print("Dominanta danych wejsciowych wynosi: {}".format(stats.mode(dane)))
print("Odchylenie standardowe danych wejsciowych wynosi: {}".format(np.std(dane)))
print("Wariancja danych wejsciowych wynosi: {}".format(np.var(dane)))
print("Skosnosc danych wejsciowych wynosi: {}".format(stats.skew(dane)))
print("Kurtoza danych wejsciowych wynosi: {}".format(stats.kurtosis(dane)))