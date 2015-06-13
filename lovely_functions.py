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

def all_you_need_is(L, O, V, E):
    # Params
    grid_size = (2, 8)
    tick_params = {'axis':'both', 'which':'both', 
                   'bottom': False, 'top':False, 
                   'left': False, 'right': False,
                   'labelbottom': False, 'labelleft': False}
    # L
    l = plt.subplot2grid(grid_size, (0, 0), rowspan=2, colspan=2)
    x, y = L()
    l.set_title(r'$y = \frac{1}{x}$')
    l.plot(x, y, 'r')
    l.tick_params(**tick_params)
    l.spines['top'].set_color('none')
    l.spines['right'].set_color('none')

    # O
    o = plt.subplot2grid(grid_size, (0, 2), rowspan=2, colspan=2)
    x, y = O()
    o.set_title(r'$x^2 + y^2 = 9$')
    o.plot(x, y, 'r')
    o.plot(x, -y, 'r')
    o.tick_params(**tick_params)
    o.spines['top'].set_color('none')
    o.spines['right'].set_color('none')

    # V
    v = plt.subplot2grid(grid_size, (0, 4), rowspan=2, colspan=2)
    x, y = V()
    v.set_title(r'$ y = |-2x|$')
    v.plot(x, y, 'r')
    v.tick_params(**tick_params)
    v.spines['top'].set_color('none')
    v.spines['right'].set_color('none')
    v.spines['left'].set_position('center')

    # E
    e = plt.subplot2grid(grid_size, (0, 6), rowspan=2, colspan=2)
    x, y = E()
    e.set_title(r'$ x = -3|\sin y|$')
    e.plot(x, y, 'r')
    e.tick_params(**tick_params)
    e.spines['top'].set_color('none')
    e.spines['left'].set_color('none')

    plt.tight_layout()
    plt.show()