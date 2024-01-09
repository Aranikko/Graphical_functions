import matplotlib.pyplot as plt
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]
def linear(x_values: list[str], k:str, b:str, theme:str):
    x_list = list(map(int, x_values.split(',')))
    
    plt.plot(x, y)

    y = [int(k) * x + int(b) for x in x_list]
    if theme == "black":
        plt.style.use('dark_background')
    else:
        pass
    plt.plot(x_list, y, label='Linear Function')
    plt.title('Linear Function')
    plt.xlabel('X Axis')
    plt.ylabel('Y Axis')
    plt.legend()
    plt.savefig('Graph.png')
    plt.clf()  # Clear the current figure after saving the graph

def quadratic(x_values, n):
    x_list = list(map(int, x_values.split(',')))
    
    y = [x**n for x in x_list]

    plt.style.use('dark_background')
    plt.plot(x_list, y, label='Quadratic Function')
    plt.title('Quadratic Function')
    plt.xlabel('X Axis')
    plt.ylabel('Y Axis')
    plt.legend()
    plt.savefig('Quadratic_Graph.png')
    plt.clf()  # Clear the current figure after saving the graph







plt.title('Простой линейный график')
plt.xlabel('Ось X')
plt.ylabel('Ось Y')




plt.show()


