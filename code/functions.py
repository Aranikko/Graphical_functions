import matplotlib.pyplot as plt
import os
from matplotlib import cm
import numpy as np
plt.switch_backend('Agg')

def linear(x_values: list[str], a:str, b:str, theme:str, name_file = "linear"): # y=kx+b
    
    x_values = x_values.replace("x:", "")  
    a = a.replace("k:", "")
    b = b.replace("b:", "")
    x = list(map(int, x_values.split(',')))
    y = [int(a) * x + int(b) for x in x]
    
    plt.plot(x, y)
    if theme == "black":
        plt.style.use('dark_background')
    else:
        pass
    plt.plot(x, y, label='Linear Function')
    plt.title('Linear Function')
    plt.xlabel('X Axis')
    plt.ylabel('Y Axis')
    plt.legend()
    plt.savefig(f'{name_file}.png')
    plt.clf()  # Clear the current figure after saving the graph
    



def check_file_availability(file_name):
    return os.path.exists(file_name)

def quadratic_equation(x_values: list[str], a: str, b: str, c: str, theme: str, name_file = "quadratic_equation"): # y = ax^2 + bx + c
    x_values = x_values.replace("x:", "")
    a = a.replace("a:", "")
    b = b.replace("b:", "")
    c = c.replace("c:", "")
    
    x = list(map(int, x_values.split(',')))
    
    y = [int(a) * x**2 + int(b) * x + int(c) for x in x]
    
    plt.plot(x, y)
    
    if theme == "black":
        plt.style.use('dark_background')
    
    plt.plot(x, y, label='Quadratic Function')
    plt.title('Quadratic Function')
    plt.xlabel('X Axis')
    plt.ylabel('Y Axis')
    plt.legend()
    plt.savefig(f'{name_file}.png')
    plt.clf()  # Clear the current figure after saving the graph

def cubic_function(x_values, theme='default', name_file='Cubic_Function_Graph'): #  y = x^3
    """
    Plots a graph for y = x^3.

    Parameters:
    - x_values: List of x coordinates.
    - theme: Theme of the plot. Supports 'default' and 'dark'.
    - name_file: Name of the file to save the graph.
    """
    x = list(map(int, x_values.split(',')))
    y = [x_val**3 for x_val in x]

    plt.plot(x, y)

    if theme == 'dark':
        plt.style.use('dark_background')

    plt.plot(x, y, label='Cubic Function')
    plt.title('Cubic Function: y = x^3')
    plt.xlabel('X Axis')
    plt.ylabel('Y Axis')
    plt.legend()
    plt.savefig(f'{name_file}.png')
    plt.clf()  # Clear the current figure after saving the graph

import math

def square_root_function(x_values, theme='default', name_file='Square_Root_Function_Graph'): # y = sqrt(x)
    """
    Plots a graph for y = sqrt(x).

    Parameters:
    - x_values: List of x coordinates.
    - theme: Theme of the plot. Supports 'default' and 'dark'.
    - name_file: Name of the file to save the graph.
    """
    x = list(map(int, x_values.split(',')))
    y = [math.sqrt(x_val) for x_val in x]

    plt.plot(x, y)

    if theme == 'dark':
        plt.style.use('dark_background')

    plt.plot(x, y, label='Square Root Function')
    plt.title('Square Root Function: y = sqrt(x)')
    plt.xlabel('X Axis')
    plt.ylabel('Y Axis')
    plt.legend()
    plt.savefig(f'{name_file}.png')
    plt.clf()  # Clear the current figure after saving the graph

def reciprocal_function(x_values, theme='default', name_file='Reciprocal_Function_Graph'): # y = 1/x
    """
    Plots a graph for y = 1/x.

    Parameters:
    - x_values: List of x coordinates.
    - theme: Theme of the plot. Supports 'default' and 'dark'.
    - name_file: Name of the file to save the graph.
    """
    x = list(map(int, x_values.split(',')))
    y = [1/x_val for x_val in x if x_val != 0]

    plt.plot(x, y)

    if theme == 'dark':
        plt.style.use('dark_background')

    plt.plot(x, y, label='Reciprocal Function')
    plt.title('Reciprocal Function: y = 1/x')
    plt.xlabel('X Axis')
    plt.ylabel('Y Axis')
    plt.legend()
    plt.savefig(f'{name_file}.png')
    plt.clf()  # Clear the current figure after saving the graph
    


def natural_log_function(x_values, theme='default', name_file='Natural_Log_Function_Graph'): # y = lg(x)
    """
    Plots a graph for y = ln(x) (natural logarithm of x).

    Parameters:
    - x_values: List of x coordinates.
    - theme: Theme of the plot. Supports 'default' and 'dark'.
    - name_file: Name of the file to save the graph.
    """
    x = np.array(list(map(float, x_values.split(','))))
    y = np.log(x)

    plt.plot(x, y)

    if theme == 'dark':
        plt.style.use('dark_background')

    plt.plot(x, y, label='Natural Log Function')
    plt.title('Natural Log Function: y = ln(x)')
    plt.xlabel('X Axis')
    plt.ylabel('Y Axis')
    plt.legend()
    plt.savefig(f'{name_file}.png')
    plt.clf()  # Clear the current figure after saving the graph
    
def sine_function(x_values, theme='default', name_file='Sine_Function_Graph'): # y = sin(x)
    """
    Plots a graph for y = sin(x).

    Parameters:
    - x_values: List of x coordinates.
    - theme: Theme of the plot. Supports 'default' and 'dark'.
    - name_file: Name of the file to save the graph.
    """
    x = np.array(list(map(float, x_values.split(','))))
    y = np.sin(x)

    plt.plot(x, y)

    if theme == 'dark':
        plt.style.use('dark_background')

    plt.plot(x, y, label='Sine Function')
    plt.title('Sine Function: y = sin(x)')
    plt.xlabel('X Axis')
    plt.ylabel('Y Axis')
    plt.legend()
    plt.savefig(f'{name_file}.png')
    plt.clf()  # Clear the current figure after saving the graph
    
def tangent_function(x_values, theme='default', name_file='Tangent_Function_Graph'): # y = tg(x)
    """
    Plots a graph for y = tan(x).

    Parameters:
    - x_values: List of x coordinates.
    - theme: Theme of the plot. Supports 'default' and 'dark'.
    - name_file: Name of the file to save the graph.
    """
    x = np.array(list(map(float, x_values.split(','))))
    y = np.tan(x)

    plt.plot(x, y)

    if theme == 'dark':
        plt.style.use('dark_background')

    plt.plot(x, y, label='Tangent Function')
    plt.title('Tangent Function: y = tan(x)')
    plt.xlabel('X Axis')
    plt.ylabel('Y Axis')
    plt.legend()
    plt.savefig(f'{name_file}.png')
    plt.clf()  # Clear the current figure after saving the graph
    

def cotangent_function(x_values, theme='default', name_file='Cotangent_Function_Graph'): # y = ctg(x)
    """
    Plots a graph for y = cot(x).

    Parameters:
    - x_values: List of x coordinates.
    - theme: Theme of the plot. Supports 'default' and 'dark'.
    - name_file: Name of the file to save the graph.
    """
    x = np.array(list(map(float, x_values.split(','))))
    y = 1 / np.tan(x)

    plt.plot(x, y)

    if theme == 'dark':
        plt.style.use('dark_background')

    plt.plot(x, y, label='Cotangent Function')
    plt.title('Cotangent Function: y = cot(x)')
    plt.xlabel('X Axis')
    plt.ylabel('Y Axis')
    plt.legend()
    plt.savefig(f'{name_file}.png')
    plt.clf()  # Clear the current figure after saving the graph

def arcsine_function(x_values, theme='default', name_file='Arcsine_Function_Graph'): # y = arcsin(x)
    """
    Plots a graph for y = arcsin(x) (inverse sine function).

    Parameters:
    - x_values: List of x coordinates.
    - theme: Theme of the plot. Supports 'default' and 'dark'.
    - name_file: Name of the file to save the graph.
    """
    x = np.array(list(map(float, x_values.split(','))))
    y = np.arcsin(x)

    plt.plot(x, y)

    if theme == 'dark':
        plt.style.use('dark_background')

    plt.plot(x, y, label='Arcsine Function')
    plt.title('Arcsine Function: y = arcsin(x)')
    plt.xlabel('X Axis')
    plt.ylabel('Y Axis')
    plt.legend()
    plt.savefig(f'{name_file}.png')
    plt.clf()  # Clear the current figure after saving the graph
    
def arccosine_function(x_values, theme='default', name_file='Arccosine_Function_Graph'): # y = arccos(x)
    """
    Plots a graph for y = arccos(x) (inverse cosine function).

    Parameters:
    - x_values: List of x coordinates.
    - theme: Theme of the plot. Supports 'default' and 'dark'.
    - name_file: Name of the file to save the graph.
    """
    x = np.array(list(map(float, x_values.split(','))))
    y = np.arccos(x)

    plt.plot(x, y)

    if theme == 'dark':
        plt.style.use('dark_background')

    plt.plot(x, y, label='Arccosine Function')
    plt.title('Arccosine Function: y = arccos(x)')
    plt.xlabel('X Axis')
    plt.ylabel('Y Axis')
    plt.legend()
    plt.savefig(f'{name_file}.png')
    plt.clf()  # Clear the current figure after saving the graph    

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

def product_function(x_values, y_values, name_file='3D_Plot_Graph'): # z = x*y
    x = np.array(list(map(float, x_values.split(','))))
    y = np.array(list(map(float, y_values.split(','))))
    X, Y = np.meshgrid(x, y)
    Z = X * Y

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(X, Y, Z, cmap='viridis')

    ax.set_xlabel('X Axis')
    ax.set_ylabel('Y Axis')
    ax.set_zlabel('Z Axis')
    ax.set_title('3D Plot: z = x * y')

    plt.savefig(f'{name_file}.png')
    plt.clf()  # Clear the current figure after saving the graph
    
def sine_product_function(x_values, name_file='3D_Sine_Plot_Graph'): # z = sin(x)
    x = np.array(list(map(float, x_values.split(','))))
    y = np.sin(x)
    X, Y = np.meshgrid(x, y)
    Z = np.sin(X)

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(X, Y, Z, cmap='viridis')

    ax.set_xlabel('X Axis')
    ax.set_ylabel('Y Axis')
    ax.set_zlabel('Z Axis')
    ax.set_title('3D Plot: z = sin(x)')

    plt.savefig(f'{name_file}.png')
    plt.clf()  # Clear the current figure after saving the graph

def sine_cosine_product_function(x_values, y_values, name_file='3D_Sin_Cos_Plot_Graph'):  # z=sin(x)cos(y)
    x = np.array(list(map(float, x_values.split(','))))
    y = np.array(list(map(float, y_values.split(','))))
    X, Y = np.meshgrid(x, y)
    Z = np.sin(X) * np.cos(Y)

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(X, Y, Z, cmap='viridis')

    ax.set_xlabel('X Axis')
    ax.set_ylabel('Y Axis')
    ax.set_zlabel('Z Axis')
    ax.set_title('3D Plot: z = sin(x) * cos(y)')

    plt.savefig(f'{name_file}.png')
    plt.clf()  # Clear the current figure after saving the graph
    
def quadratic_product_function(x_values, y_values, name_file='Custom_3D_Plot_Graph'): # z=x2y2+2
    x = np.array(list(map(float, x_values.split(','))))
    y = np.array(list(map(float, y_values.split(','))))
    X, Y = np.meshgrid(x, y)
    Z = X**2 * Y**2 + 2

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(X, Y, Z, cmap='viridis')

    ax.set_xlabel('X Axis')
    ax.set_ylabel('Y Axis')
    ax.set_zlabel('Z Axis')
    ax.set_title('3D Plot: z = x^2 * y^2 + 2')

    plt.savefig(f'{name_file}.png')
    plt.clf()  # Clear the current figure after saving the graph