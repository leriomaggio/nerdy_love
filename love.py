import matplotlib.pyplot as plt

def truly(L, O, V, E):
    # Params
    grid_size = (2, 8)
    tick_params = {'axis':'both', 'which':'both', 
                   'bottom': False, 'top':False, 
                   'left': False, 'right': False,
                   'labelbottom': False, 'labelleft': False}
                   
    line_width = 4
    # L
    l = plt.subplot2grid(grid_size, (0, 0), rowspan=2, colspan=2)
    x, y = L()
    l.set_title(r'$y = \frac{1}{x}$')
    l.plot(x, y, 'r', lw=line_width)
    l.tick_params(**tick_params)
    l.spines['top'].set_color('none')
    l.spines['right'].set_color('none')

    # O
    o = plt.subplot2grid(grid_size, (0, 2), rowspan=2, colspan=2)
    x, y = O()
    o.set_title(r'$x^2 + y^2 = 9$')
    o.plot(x, y, 'r', lw=line_width)
    o.plot(x, -y, 'r', lw=line_width)
    o.tick_params(**tick_params)
    o.spines['top'].set_color('none')
    o.spines['right'].set_color('none')

    # V
    v = plt.subplot2grid(grid_size, (0, 4), rowspan=2, colspan=2)
    x, y = V()
    v.set_title(r'$ y = |-2x|$')
    v.plot(x, y, 'r', lw=line_width)
    v.tick_params(**tick_params)
    v.spines['top'].set_color('none')
    v.spines['right'].set_color('none')
    v.spines['left'].set_position('center')

    # E
    e = plt.subplot2grid(grid_size, (0, 6), rowspan=2, colspan=2)
    x, y = E()
    e.set_title(r'$ x = -3|\sin y|$')
    e.plot(x, y, 'r', lw=line_width)
    e.tick_params(**tick_params)
    e.spines['top'].set_color('none')
    e.spines['left'].set_color('none')

    plt.tight_layout()
    plt.show()
    
def my(heart):
    r, t = heart
    plt.polar(r, t, 'r', lw=5)
    tick_params = {'axis':'y', 'which':'both', 
                   'bottom': False, 'top':False, 
                   'left': False, 'right': False,
                   'labelbottom': False, 'labelleft': False}
                   
    plt.tick_params(**tick_params)
    plt.show()