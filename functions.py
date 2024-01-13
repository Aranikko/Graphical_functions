import matplotlib.pyplot as plt
import os
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


