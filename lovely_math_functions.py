import numpy as np
import matplotlib.pyplot as plt

def L():
    """ L : y = \\frac{1}{x} """
    x = np.arange(0.05, 2, 0.005)
    y = 1/x
    #p = ax.plot(x, y, 'r')
    return x, y
    

def O():
    """ O : x^2 + y^2 = 9 """
    x = np.arange(-3.0, 3, .0005)
    y = np.sqrt(9-x**2)

    #p1 = plt.plot(x, y, 'r')
    #p2 = plt.plot(x, -y, 'r')
    return x, y
    

def V():
    """ V: y = |-2x| """    
    x = np.arange(-1, 1, 0.01)
    y = np.abs(-2*x)
    #p = plt.plot(x, y, 'r')
    return x, y
    

def E():
    """ E: x = -3|\sin y|"""
    y = np.arange(-3, 3, .001)
    x = -3*np.abs(np.sin(y))
    #p = plt.plot(x, y, 'r')
    return x, y
    
    
def U():
    """ U : y = x^2 """
    x = np.arange(0.05, 2, 0.005)
    y = x**2
    #p = ax.plot(x, y, 'r')
    return x, y
    

def heart():
    t = np.arange(0,2*np.pi,.01)
    r = 2 - 2 * np.sin(t) + np.sin(t) * np.sqrt(np.abs(np.cos(t))) / (np.sin(t) + 1.4)
    return t, r