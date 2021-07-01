import tkinter as tk
from NewCalculator import *

root = tk()
root.title("Calculator")
calculatorSize = tk.Entry( width=35,borderwidth=5)
calculatorSize.grid(row=0,column=0,columnspan=3, padx=10,pady=10)

button1 = tk.Button(text="1")