import numpy as np
import matplotlib.pyplot as plt

def pltgrph(begin, end, h, f):
    elms = int(end/h)
    spc = (end - begin)/3
    x = np.linspace(begin - spc, end + spc, elms + 1)
    y = np.linspace(min(f(x)) - spc, max(f(x) + spc), elms + 1)
    plt.plot(x, f(x))
    plt.plot(x, np.linspace(0, 0, elms+ 1), color='black', linestyle='dotted')
    plt.plot(np.linspace(end, end, elms+1), np.linspace(0, f(end), elms+1), linestyle="--", color='red')
    plt.plot(np.linspace(begin, begin, elms+1), np.linspace(0, f(begin), elms+1), linestyle='--', color='red')
    plt.show()
    plt.grid()

pltgrph(0, 3, 0.1, lambda x: pow(x, 2))
