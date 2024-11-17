from tkinter import *
from tkinter import ttk

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

a = StringVar()
aEntry = ttk.Entry(inputFrame, width=5, textvariable=a)
ttk.Label(inputFrame, text="Enter lower bound:").grid(column=3, row=0)
aEntry.grid(column=3, row=1)

b = StringVar()
bEntry = ttk.Entry(inputFrame, width=5, textvariable=b)
ttk.Label(inputFrame, text="Enter upper bound:").grid(column=4, row=0)
bEntry.grid(column=4, row=1)

dx = StringVar()
dx.set("0.01")
dxEntry = ttk.Entry(inputFrame, width=5, textvariable=dx)
ttk.Label(inputFrame, text="Enter degree of accuracy:").grid(column=5, row=0)
dxEntry.grid(column=5, row=1)

detailText = "Constraints:\n\n1. Enter f(x) using Python Syntax.\n2. Use np.<func/const> for mathematical functions and constants."
details = ttk.Label(inputFrame, text=detailText)
details.grid(columnspan=5, column=0, row=2)

comButton = ttk.Button(inputFrame, text="Compute")
comButton.grid(column=5, row=2, rowspan=2, sticky=(N, W, E, S))

graphFrame = ttk.Frame(mainframe, borderwidth=5, relief="ridge")
graphFrame.grid(column= 0, row= 3, columnspan=6, sticky=(N, W, E, S))

for child in inputFrame.winfo_children():
    child.grid_configure(padx=5, pady=5)

for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)

functionEntry.focus()
root.mainloop()