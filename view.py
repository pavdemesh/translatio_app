"""View Module for Translation Management App"""

import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox


class View(tk.Tk):
    """This Class handles the representation of data"""
    """
    self.treeview_frame
    self.treeview_scroll
    self.data_treeview
    """
    # Size of Padding
    PAD_VALUE = 10

    # For the instantiation of View object we need to pass the Controller object
    def __init__(self, controller):
        super().__init__()
        self.controller = controller

        self._configure_style()
        self._create_treeview_frame()
        self._create_treeview_scrollbar()
        self._create_treeview()
        self._bind_treeview_and_scroll()

    def main(self):
        self.title("Translation Management App")
        self.mainloop()

    # Configure Style of the Window and the Treeview
    def _configure_style(self):
        self.geometry('1200x700')
        style = ttk.Style()
        # Add a Theme
        style.theme_use('default')

        # Configure the Treeview Colors
        style.configure('Treeview',
                        background='#3D3D3',
                        foreground='black',
                        rowheight=25,
                        fieldbackground='#D3D3D3')

        # Change Color of Selected Row
        style.map('Treeview', background=[('selected', '#347083')])

    # Create Treeview Frame
    def _create_treeview_frame(self):
        self.treeview_frame = tk.Frame(self)
        self.treeview_frame.pack(padx=self.PAD_VALUE, pady=self.PAD_VALUE)

    # Create Treeview Scrollbar
    def _create_treeview_scrollbar(self):
        self.treeview_scroll = tk.Scrollbar(self.treeview_frame)
        self.treeview_scroll.pack(side="right", fill="y")

    # Create Treeview
    def _create_treeview(self):
        self.data_treeview = ttk.Treeview(self.treeview_frame, yscrollcommand=self.treeview_scroll.set,
                                          selectmode='extended')
        self.data_treeview.pack()

    def _bind_treeview_and_scroll(self):
        self.treeview_scroll.configure(command=self.data_treeview.yview)
