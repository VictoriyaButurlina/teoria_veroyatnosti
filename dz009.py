# Задача 1 Даны значения величины заработной платы заемщиков банка (zp) и значения их
# поведенческого кредитного скоринга (ks): zp = [35, 45, 190, 200, 40, 70, 54, 150, 120, 110],
# ks = [401, 574, 874, 919, 459, 739, 653, 902, 746, 832]. Используя математические
# операции, посчитать коэффициенты линейной регрессии, приняв за X заработную плату
# (то есть, zp - признак), а за y - значения скорингового балла (то есть, ks - целевая
# переменная). Произвести расчет как с использованием intercept, так и без.

import numpy as np
import pandas as pd
from scipy import stats

import matplotlib.pyplot as plt
zp = np.array([35, 45, 190, 200, 40, 70, 54, 150, 120, 110])
ks = np.array([401, 574, 874, 919, 459, 739, 653, 902, 746, 832])

b=(np.mean(zp * ks) - np.mean(zp) * np.mean(ks)) / (np.mean(zp**2) - np.mean(zp) ** 2)
a=np.mean(ks)-b*np.mean(zp)

plt.scatter(zp,ks)
plt.plot(zp, a+b*zp, c='r')
plt.xlabel('Величина заработной платы')
plt.ylabel('Поведенческий кредитный скоринг', rotation=90)
plt.show()
print('Полученная функция наглядно описывает линейную взаимосвязь между величиной заработной платы, и кредитного скоринга.')
# Задача 2 Посчитать коэффициент линейной регрессии при заработной плате (zp), используя
# градиентный спуск (без intercept).

def _mse(b, x, y):
    return np.sum((b*x-y)**2)/len(x)
_mse(2.62, zp, ks)
print(_mse)
def _mse_p(b,x,y):
    return (2/len(x))*np.sum((b*x-y)*x)
alpha=1e-06
b=0.1
mse_min=_mse(b,zp,ks)
i_min=1
b_min=b
for i in range(10000):
    b-=alpha*_mse_p(b,zp,ks)
    if i%100==0:
        print(f'Итерация #{i}, b={b}, mse={_mse(b, zp,ks)}')
    if _mse(b,zp,ks)>mse_min:
        print(f'Итерация #{i_min}, b={b_min}, mse={mse_min},\nДостигнут минимум.')
        break
    else:
        mse_min=_mse(b,zp,ks)
        i_min=i
        b_min=b
print(b_min)  
