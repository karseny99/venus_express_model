from math import *
from matplotlib import pyplot as plt
import json


with open('data.txt', 'r') as fr:   # Читаем данные с прошлого этапа
    previousValues = json.load(fr)

with open("plt.txt") as f:
    p = [x.split() for x in f.read().split("\n")][:-1]


# Константы

G = 6.6743 * 10 ** (-11)
M_venus = 5.9742 * 10 ** 24
R_venus = 6371000
g = 9.8
S = 10.3 ** 2 * pi / 4  # Площадь обтекателя
m0 = 96752  # Масса ракеты
c = 0.03
flight_time_2 = 182
angle = (15 * pi / 180) / flight_time_2
ang = 61 * pi / 180

# Характеристики ракеты

Ft2_vacuum = 94 * 9800
m_release = 310.0


dt = 0.01



def getValues(previousValues):
    for i in range(int(flight_time_2 / dt)):
        # if i == 15780:
        #     global m0
        #     m0 = 94852
        v = previousValues[-1][-2][0] ** 2 + previousValues[-1][-2][1] ** 2
        acc_x = acceleration_x(dt * i, sqrt(v), previousValues[-1][-1][1])
        acc_y = acceleration_y(dt * i, sqrt(v), previousValues[-1][-1][1])
        speed_x = euler(previousValues[-2][-2][0], acc_x)
        speed_y = euler(previousValues[-2][-2][1], acc_y)
        coord_x = euler(previousValues[-2][-1][0], previousValues[-1][-2][0])
        coord_y = euler(previousValues[-2][-1][1], previousValues[-1][-2][1])
        previousValues.append([[acc_x, acc_y], [speed_x, speed_y], [coord_x, coord_y]])
        #print(F_resistance(v, coord_y))

def acceleration_x(t, v, h):
    return (Ft2_vacuum * sin(ang + angle * t)) / (m0 - m_release * t)

def acceleration_y(t, v, h):
    return (Ft2_vacuum * cos(ang + angle * t)) / (m0 - m_release * t) - g

def euler(x, y):
    return x + 2 * dt * y


# Сила сопротивления воздуха

def p_env(h):
    for u in range(1, len(p) - 1):
        if float(p[u][0]) > h:
            return float(p[u - 1][1])
    return 0


def F_resistance(v, h):
    return (c * S * p_env(h) * (v ** 2)) / 2

getValues(previousValues)
for i in previousValues:
    print(i)
with open('data.txt', 'w') as fw:
    json.dump(previousValues, fw)
























































