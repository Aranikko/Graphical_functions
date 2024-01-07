x = []
y = []
k = 1
b = 0

import matplotlib.pyplot as plt
from math import *

def linear(x, k, b):
    x_list = list(map(int, filter(None, x.value.split(','))))
            
    plt.style.use('dark_background')
    
    y = []

    for i in range(len(x_list)):
        y.append(int(k.value) * x_list[i] + int(b.value))

    plt.plot(x_list, y, label=' ')
    plt.title(' ')
    plt.xlabel('Ось X')
    plt.ylabel('Ось Y')
    plt.legend()
    plt.savefig('Graph.png')
    


