import tkinter
from tkinter import font

root = tkinter.Tk()  # Start Tk instance
your_font = font.nametofont("TkDefaultFont")  # Get default font value into Font object
print(your_font.actual())
