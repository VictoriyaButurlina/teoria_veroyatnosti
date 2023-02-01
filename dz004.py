# Задача 1. Случайная непрерывная величина A имеет равномерное распределение на
# промежутке (200, 800].
# Найдите ее среднее значение и дисперсию.

def mean_varience(a,b):
    return f'мат ожидание = {(a+b)/2:.2f} дисперсия = {((b-a)**2)/12:.2f}'

print(mean_varience(200, 800))
print()
# Задача 2. О случайной непрерывной равномерно распределенной величине B известно, что ее
# дисперсия равна 0.2.
# Можно ли найти правую границу величины B и ее среднее значение зная, что левая
# граница равна 0.5?
# Если да, найдите ее.
pr_granica=2.4**0.5+0.5
print(f'Правая граница величины B = {pr_granica:.4f}')
print(f'Среднее значение = {(0.5+pr_granica)/2:.4f}')
print()
# Задача 3. Непрерывная случайная величина X распределена нормально и задана плотностью
# распределения
# f(x) = (1 / (4 * sqrt(2pi))) * exp((-(x+2)**2) / 32)
# Найдите:
# а). M(X)
# б). D(X)
# в). std(X) (среднее квадратичное отклонение)
print(f'Мат ожидание = -2') 
print(f'Дисперсия = 16') #сигма = 4, D = 4**2
print(f'СКО = 4') 
print()
# Задача 4. Рост взрослого населения города X имеет нормальное распределение, причем, средний рост равен 174 см, 
# а среднее квадратическое отклонение равно 8 см. 
# посчитайте, какова вероятность того, что случайным образом выбранный взрослый человек имеет рост:
# 1. больше 182 см?
# 2. больше 190 см?
# 3. от 166 см до 190 см?
# 4. от 166 см до 182 см?
# 5. от 158 см до 190 см?
# 6. не выше 150 см или не ниже 190 см?
# 7. не выше 150 см или не ниже 198 см?
# 8. ниже 166 см?
# Задачу можно решить двумя способами: без использования сторонних библиотек (numpy, scipy, pandas и пр.), а затем проверить себя с помощью встроенных функций
from scipy import stats

print(f'вер-ть, что рост больше 182 см - {(1-stats.norm.cdf(182, loc = 174, scale = 8)):.4f}')
print(f'вер-ть, что рост больше 190 см - {(1-stats.norm.cdf(190, loc = 174, scale = 8)):.4f}')
print(f'вер-ть, что рост от 166 см до 190 см - {(stats.norm.cdf(190, loc = 174, scale = 8)-stats.norm.cdf(166, loc = 174, scale = 8)):.4f}')
print(f'вер-ть, что рост от 166 см до 182 см - {(stats.norm.cdf(182, loc = 174, scale = 8)-stats.norm.cdf(166, loc = 174, scale = 8)):.4f}')
print(f'вер-ть, что рост от 158 см до 190 см - {(stats.norm.cdf(190, loc = 174, scale = 8)-stats.norm.cdf(158, loc = 174, scale = 8)):.4f}')
print(f'вер-ть, что рост не выше 150 см или не ниже 190 см - {(stats.norm.cdf(150, loc = 174, scale = 8)+(1-stats.norm.cdf(190, loc = 174, scale = 8))):.4f}')
print(f'вер-ть, что рост не выше 150 см или не ниже 198 см - {(stats.norm.cdf(150, loc = 174, scale = 8)+(1-stats.norm.cdf(198, loc = 174, scale = 8))):.4f}')
print(f'вер-ть, что рост ниже 166 см - {(stats.norm.cdf(166, loc = 174, scale = 8)):.4f}')
print()


# Задача 5. На сколько сигм (средних квадратичных отклонений) отклоняется рост человека,
# равный 190 см, от
# математического ожидания роста в популяции, в которой M(X) = 178 см и D(X) = 25 кв.см?
print(f'Рост человека отклоняется на - {(190-178)/25**0.5} сигм')
print()
# Дополнительно (на повторение)
# Даны значения зарплат из выборки выпускников:
# 100, 80, 75, 77, 89, 33, 45, 25, 65, 17, 30, 24, 57, 55, 70, 75, 65, 84, 90, 150.
# построить гистограмму распределения, подобрав лучший параметр bins,
# найти первый и третий квартили, интерквартильное расстояние. Найти выбросы в выборке, используя для этого "усы" из boxplot.
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

zp = np.array([100, 80, 75, 77, 89, 33, 45, 25, 65, 17, 30, 24, 57, 55, 70, 75, 65, 84, 90, 150]) #1-й способ Numpy
plt.hist(zp, bins=15)
plt.show() 

zp_2= pd.DataFrame([100, 80, 75, 77, 89, 33, 45, 25, 65, 17, 30, 24, 57, 55, 70, 75, 65, 84, 90, 150]) #2-й способ Pandas
zp_2.hist (bins = 20)
plt.show() 
zp_2.boxplot()
plt.show() 