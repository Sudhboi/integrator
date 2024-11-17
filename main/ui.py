from tkinter import *
from tkinter import ttk
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.figure import Figure 
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk) 

def integral(f, begin, end, dx):
    area = 0
    for i in [begin + dx*n for n in range(int((end - begin)/dx))]:
        area += (f(i)*(dx)) + (0.5 * dx * (f(i + dx) - f(i)))
    return area

def pltgrph(f, begin, end, h):
    fig = plt.figure(1)
    plt.ion()
    elms = int(end/h)
    spc = (end - begin)/3
    x = np.linspace(begin - spc, end + spc, elms + 1)
    y = np.linspace(min(f(x)) - spc, max(f(x) + spc), elms + 1)
    plt.plot(x, f(x))
    plt.plot(x, np.linspace(0, 0, elms+ 1), color='black', linestyle='dotted')
    plt.plot(np.linspace(end, end, elms+1), np.linspace(0, f(end), elms+1), linestyle="--", color='red')
    plt.plot(np.linspace(begin, begin, elms+1), np.linspace(0, f(begin), elms+1), linestyle='--', color='red')
    plt.grid()

    canvas = FigureCanvasTkAgg(fig, master = graphFrame)
    plot_widget = canvas.get_tk_widget()
    plot_widget.grid(row=0, column=0)   

def compute(*args):
    try:
        f = functionInput.get()
        print(f)
        a = eval(aval.get())
        b = eval(bval.get())
        dx = eval(dxval.get())
        print(a, b, dx)
        integralValue = round(integral(eval("lambda x: " + f), a, b, dx), 4)
        outputValue.set("The value of the integral within the given bounds is {}".format(integralValue))
        pltgrph(eval("lambda x: " + f), a, b, dx)
    except ValueError:
        pass
    except Exception as e:
        print(e)

root = Tk()
root.title("Integrator")
root.resizable(False, False)

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

inputFrame = ttk.Frame(mainframe, borderwidth=5, relief="ridge")
inputFrame.grid(column=0, row=0, sticky=(W, E), columnspan=6, rowspan=3)

functionInput = StringVar()
functionEntry = ttk.Entry(inputFrame, width=40, textvariable=functionInput)
ttk.Label(inputFrame, text="Enter f(x):").grid(column=0, row=0, columnspan=3)
functionEntry.grid(column=0, row=1, columnspan=3, sticky=(W, E))

aval = StringVar()
aEntry = ttk.Entry(inputFrame, width=9, textvariable=aval)
ttk.Label(inputFrame, text="Enter lower bound:").grid(column=3, row=0)
aEntry.grid(column=3, row=1)

bval = StringVar()
bEntry = ttk.Entry(inputFrame, width=9, textvariable=bval)
ttk.Label(inputFrame, text="Enter upper bound:").grid(column=4, row=0)
bEntry.grid(column=4, row=1)

dxval = StringVar()
dxval.set("0.01")
dxEntry = ttk.Entry(inputFrame, width=6, textvariable=dxval)
ttk.Label(inputFrame, text="Enter degree of accuracy:").grid(column=5, row=0)
dxEntry.grid(column=5, row=1)

detailText = "Constraints:\n\n1. Enter f(x) using Python Syntax.\n2. Use np.<func/const> for mathematical functions and constants."
details = ttk.Label(inputFrame, text=detailText)
details.grid(columnspan=5, column=0, row=2)

comButton = ttk.Button(inputFrame, text="Compute", command=compute)
comButton.grid(column=5, row=2, rowspan=2, sticky=(N, W, E, S))

graphFrame = ttk.Frame(mainframe, borderwidth=5, relief="ridge")
graphFrame.grid(column= 0, row= 3, columnspan=6, sticky=(N, W, E, S))

outputValue = StringVar()
outputLabel = ttk.Label(mainframe, textvariable=outputValue)
outputLabel.grid(column=0, row=4, columnspan=6)

for child in inputFrame.winfo_children():
    child.grid_configure(padx=5, pady=5)

for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)

functionEntry.focus()
root.mainloop()