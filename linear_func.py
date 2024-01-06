x = []
y = []
k = 1
b = 0

a = "1,2,3,4,5"
result_list = a.split(',')
print(result_list)  # Output: ['1', '2', '3', '4', '5']

import matplotlib.pyplot as plt
from math import *

plt.style.use('dark_background')

x = [-1, -2, -3, -4, -5,1, 2, 3, 4, 5]
y = []

for i in range(len(x)):
    y.append(k * x[i] + b)
    

# Создание линейного графика
plt.plot(x, y, label=' ')

# Добавление заголовка и меток к осям
plt.title(' ')
plt.xlabel('Ось X')
plt.ylabel('Ось Y')

# Добавление легенды
plt.legend()

# Показать график
plt.savefig('my_plot.png')
