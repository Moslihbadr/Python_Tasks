from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import Canvas
root = Tk()
root.geometry('600x300')
frm = ttk.Frame(root, padding=100)
badr = ttk.Frame(root, padding=100)
frm.grid()
badr.grid()
frame = tk.Tk()
frame.title("TextBox Input")
frame.geometry('400x200')
def printInput():
    inp = inputtxt.get(1.0, "end-1c")
    Label.config(text = "Provided Input: "+inp)

  
# Label Creation
lbl = tk.Label(frame, text = "")
lbl.pack()
frame.mainloop()
ttk.Label(frm, text="êtes-vous foukahi ?").grid(column=1, row=0)
ttk.Label(frm, text="bonjour !").grid(column=1, row=1)
ttk.Button(frm, text="Quiter", command=root.destroy).grid(column=1, row=2)
root.mainloop()
# TextBox Creation
inputtxt = tk.Text(frame,
                   height = 2,
                   width = 20)
  
inputtxt.pack()
# Button Creation
printButton = tk.Button(frame,
                        text = "Print", 
                        command = printInput)
printButton.pack()
