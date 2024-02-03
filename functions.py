import matplotlib.pyplot as plt
import os
from matplotlib import cm
import numpy as np
plt.switch_backend('Agg')

def linear(x_values: list[str], k:str, b:str, theme:str):
    
    x_values = x_values.replace("x:", "")  
    k = k.replace("k:", "")
    b = b.replace("b:", "")
    
    
    
    x = list(map(int, x_values.split(',')))
    
    

    y = [int(k) * x + int(b) for x in x]
    
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
    plt.savefig('Graph.png')
    plt.clf()  # Clear the current figure after saving the graph
    



def check_file_availability(file_name):
    return os.path.exists(file_name)

def quadratic(x_values, n):
    x_values = x_values.replace("x:", "") 
    n = n.replace("n:", "")
    
    x_list = list(map(int, x_values.split(',')))
    
    y = [x**int(n) for x in x_list]

    plt.style.use('dark_background')
    plt.plot(x_list, y, label='Quadratic Function')
    plt.title('Quadratic Function')
    plt.xlabel('X Axis')
    plt.ylabel('Y Axis')
    plt.legend()
    plt.savefig('Graph.png')
    plt.clf()  # Clear the current figure after saving the graph
    
# quadratic('4,3,1,0,-1,-3,-4', '2')


def plot_3d_surface(x_values, y_values, theme='default'):
    """
    Plots a 3D surface graph based on x, y values, with z being the product of x and y.

    Parameters:
    - x_values: List of x coordinates.
    - y_values: List of y coordinates.
    - theme: Theme of the plot. Supports 'default' and 'dark'.
    """
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Convert string inputs to lists of integers
    x = np.array(list(map(int, x_values.split(','))))
    y = np.array(list(map(int, y_values.split(','))))
    
    # Create a meshgrid for x and y values
    X, Y = np.meshgrid(x, y)
    Z = X * Y  # Calculate Z values as the product of X and Y

    # Plot a surface
    surf = ax.plot_surface(X, Y, Z, cmap=cm.Blues)

    if theme == 'dark':
        plt.style.use('dark_background')

    ax.set_xlabel('X Axis')
    ax.set_ylabel('Y Axis')
    ax.set_zlabel('Z Axis')
    plt.title('3D Surface Graph')
    plt.savefig('3D_Surface_Graph.png')
    plt.clf()  # Clear the current figure after saving the graph