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
m0 = 30693  # Масса ракеты на третьей ступени
flight_time_3 = 228
angle = (8 * pi / 180) / flight_time_3
ang = 78 * pi / 180

# Характеристики ракеты

Ft3 = 30.38 * 9800
m_release = 84.7


dt = 0.01



def getValues(previousValues):
    for i in range(int(flight_time_3 / dt)):
        v = previousValues[-1][-2][0] ** 2 + previousValues[-1][-2][1] ** 2
        acc_x = acceleration_x(dt * i, sqrt(v), previousValues[-1][-1][1])
        acc_y = acceleration_y(dt * i, sqrt(v), previousValues[-1][-1][1])
        speed_x = euler(previousValues[-2][-2][0], acc_x)
        speed_y = euler(previousValues[-2][-2][1], acc_y)
        coord_x = euler(previousValues[-2][-1][0], previousValues[-1][-2][0])
        coord_y = euler(previousValues[-2][-1][1], previousValues[-1][-2][1])
        previousValues.append([[acc_x, acc_y], [speed_x, speed_y], [coord_x, coord_y]])

def acceleration_x(t, v, h):
    return (Ft3 * sin(ang + angle * t)) / (m0 - m_release * t)

def acceleration_y(t, v, h):
    return (Ft3 * cos(ang + angle * t)) / (m0 - m_release * t) - g

def euler(x, y):
    return x + 2 * dt * y



getValues(previousValues)

for i in previousValues:
    print(i)

with open('data.txt', 'w') as fw:
    json.dump(previousValues, fw)
























































