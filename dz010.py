#  Провести дисперсионный анализ для определения того, есть ли различия среднего
# роста среди взрослых футболистов, хоккеистов и штангистов.
# Даны значения роста в трех группах случайно выбранных спортсменов:
# Футболисты: 173, 175, 180, 178, 177, 185, 183, 182.
# Хоккеисты: 177, 179, 180, 188, 177, 172, 171, 184, 180.
# Штангисты: 172, 173, 169, 177, 166, 180, 178, 177, 172, 166, 170.
import numpy as np
import pandas as pd
from scipy import stats
import matplotlib.pyplot as pyplot
football=np.array([173, 175, 180, 178, 177, 185, 183, 182])
hockey=np.array([177, 179, 180, 188, 177, 172, 171, 184, 180])
weightlifter=np.array([172, 173, 169, 177, 166, 180, 178, 177, 172, 166, 170])

pyplot.boxplot([football, hockey, weightlifter])
pyplot.show()

#тест на нормальность, p-value больше альфа
print(stats.shapiro(football))
print(stats.shapiro(hockey))
print(stats.shapiro(weightlifter))

print(stats.f_oneway(football, hockey, weightlifter))
print('p-value < альфа ->> гипотеза отвергается с вероятностью ошибки альфа, рост взрослых футболистов, хоккеистов и штангистов различен')

