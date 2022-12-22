import json
from math import atan, cos, sqrt
from matplotlib import pyplot as plt
from numpy import arange
R_earth = 6371000

plt.style.use('ggplot')

with open('data.txt', 'r') as fr:   # Читаем данные с прошлого этапа
    previousValues = json.load(fr)

def trajectoryCorrection(x, y):
    h = R_earth * (1 / cos(atan(x / R_earth)) - 1)
    return y + h


x = [trajectoryCorrection(x[-1][0], x[-1][1]) for x in previousValues]
y = [x[-1][0] for x in previousValues]
a = [sqrt(x[0][1] ** 2 + x[0][0] ** 2) for x in previousValues]
v = [sqrt(x[1][1] ** 2 + x[1][0] ** 2) for x in previousValues]

plt.rcParams.update({'font.size': 8})
plt.subplot(2, 1, 1)
plt.plot(y, x)
plt.title("y(x)")



t = list(arange(0, 528.02, 0.01))

plt.subplot(2, 2, 3)
plt.plot(t, a)
plt.title("Ускорение(t)")

plt.subplot(2, 2, 4)
plt.plot(t, y)
plt.title("Высота(t)")

# plt.title("Скорость(t)")
# plt.plot(t, v)


plt.show()




















