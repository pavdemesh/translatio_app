"""View Module for Translation Management App"""

import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
from PIL import ImageTk, Image


class View(tk.Tk):
    """This Class handles the representation of data"""
    """
    self.treeview_frame
    self.treeview_scroll
    self.data_treeview
    """
    # Size of Padding
    PAD_VALUE = 10

    # Tuple containing column names
    COLUMN_NAMES = ("ID", "Description", "Subject", "Source Lang", "Target Lang", "Year", "Month", "Client",
                    "Source File", "Target File", "Quantity", "Unit")

    # List with Treeview column properties as dictionary entries
    TREEVIEW_COLUMNS_PROPERTIES = [
        {'name': 'ID', 'width': 40, 'minwidth': 25, 'anchor': 'center'},
        {'name': 'Description', 'width': 140, 'minwidth': 50, 'anchor': 'w'},
        {'name': 'Subject', 'width': 140, 'minwidth': 50, 'anchor': 'w'},
        {'name': 'Source Lang', 'width': 70, 'minwidth': 35, 'anchor': 'center'},
        {'name': 'Target Lang', 'width': 70, 'minwidth': 35, 'anchor': 'center'},
        {'name': 'Year', 'width': 50, 'minwidth': 35, 'anchor': 'center'},
        {'name': 'Month', 'width': 50, 'minwidth': 35, 'anchor': 'center'},
        {'name': 'Client', 'width': 100, 'minwidth': 50, 'anchor': 'center'},
        {'name': 'Source File', 'width': 140, 'minwidth': 50, 'anchor': 'w'},
        {'name': 'Target File', 'width': 140, 'minwidth': 50, 'anchor': 'w'},
        {'name': 'Quantity', 'width': 60, 'minwidth': 35, 'anchor': 'center'},
        {'name': 'Unit', 'width': 60, 'minwidth': 35, 'anchor': 'center'},
    ]

    # List with Treeview heading properties asa dictionary entries
    TREEVIEW_HEADINGS = [
        {'col_name': 'ID', 'head_name': 'ID', 'anchor': 'center'},
        {'col_name': 'Description', 'head_name': 'Description', 'anchor': 'center'},
        {'col_name': 'Subject', 'head_name': 'Subject', 'anchor': 'center'},
        {'col_name': 'Source Lang', 'head_name': 'Source Lang', 'anchor': 'center'},
        {'col_name': 'Target Lang', 'head_name': 'Target Lang', 'anchor': 'center'},
        {'col_name': 'Year', 'head_name': 'Year', 'anchor': 'center'},
        {'col_name': 'Month', 'head_name': 'Month', 'anchor': 'center'},
        {'col_name': 'Client', 'head_name': 'Client', 'anchor': 'center'},
        {'col_name': 'Source File', 'head_name': 'Source File', 'anchor': 'center'},
        {'col_name': 'Target File', 'head_name': 'Target File', 'anchor': 'center'},
        {'col_name': 'Quantity', 'head_name': 'Quantity', 'anchor': 'center'},
        {'col_name': 'Unit', 'head_name': 'Unit', 'anchor': 'center'}
    ]

    # For the instantiation of View object we need to pass the Controller object
    def __init__(self, controller):
        super().__init__()
        self.controller = controller

        # Configure Style
        self._configure_style()
        # Create Treeview Frame
        self._create_treeview_frame()
        # Create Treeview Scrollbar
        self._create_treeview_scrollbar()
        # Create Treeview
        self._create_treeview()
        # Connect Treeview to Scrollbar
        self._bind_treeview_and_scroll()
        # Set Treeview Columns
        self._configure_treeview_cols(self.COLUMN_NAMES, self.TREEVIEW_COLUMNS_PROPERTIES)
        # Set Treeview Headings
        self._configure_treeview_headings(self.TREEVIEW_HEADINGS)
        # Set Color for Odd and Even Rows
        self._configure_color_odd_even_row()
        # Create Frame for Entry Boxes and Labels
        self._create_entry_boxes_frame()
        # Create Entry Boxes in the Entry Frame
        self._create_entry_boxes()

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

    # Configure Treeview columns
    def _configure_treeview_cols(self, column_names, column_properties):
        self.data_treeview['columns'] = column_names
        # Configure 0st invisible column
        self.data_treeview.column("#0", width=0, stretch=False)
        # Set column properties based on data in the provided list
        for column in column_properties:
            self.data_treeview.column(column['name'], width=column['width'],
                                      minwidth=column['minwidth'], anchor=column['anchor'])

    # Configure Treeview headings
    def _configure_treeview_headings(self, heading_properties):
        # Configure 0st invisible column
        self.data_treeview.heading("#0", text="", anchor='center')
        # Set headings based on data in the provided list
        for heading in heading_properties:
            self.data_treeview.heading(heading['col_name'], text=heading['head_name'], anchor=heading['anchor'])

    # Configure the Color for Odd and Even Rows
    def _configure_color_odd_even_row(self):
        self.data_treeview.tag_configure('oddrow', background='white')
        self.data_treeview.tag_configure('evenrow', background='lightblue')

    # Create Frame for Entry Boxes and Labels
    def _create_entry_boxes_frame(self):
        self.entry_boxes_frame = tk.LabelFrame(self, text="Data Fields")
        self.entry_boxes_frame.pack()

    def _create_entry_boxes(self):
        # Create Labels and Entry Boxes for Row 0
        self.description_label = tk.Label(self.entry_boxes_frame, text='Description')
        self.description_label.grid(row=0, column=0, sticky='e')

        self.description_entry = tk.Entry(self.entry_boxes_frame, width=30)
        self.description_entry.grid(row=0, column=1, sticky='w')

        # create data label (widget) and place it within first block
        self.subject_label = tk.Label(self.entry_boxes_frame, text='Subject')
        self.subject_label.grid(row=0, column=2, sticky='e')

        self.subject_entry = tk.Entry(self.entry_boxes_frame, width=30)
        self.subject_entry.grid(row=0, column=3, sticky='w')

        # create data label (widget) and place it within first block
        self.source_lang_label = tk.Label(self.entry_boxes_frame, text='Source \nLanguage')
        self.source_lang_label.grid(row=0, column=4, sticky='e')

        self.source_lang_combobox = ttk.Combobox(self.entry_boxes_frame, values=['', 'DE', 'EN', 'RU', 'UA'], width=15)
        self.source_lang_combobox.grid(row=0, column=5, sticky='w')

        # create data label (widget) and place it within first block
        self.target_lang_label = tk.Label(self.entry_boxes_frame, text='Target \nLanguage')
        self.target_lang_label.grid(row=0, column=6, sticky='w')

        self.target_lang_combobox = ttk.Combobox(self.entry_boxes_frame, values=['', 'DE', 'EN', 'RU', 'UA'], width=15)
        self.target_lang_combobox.grid(row=0, column=7, sticky='w')
        # Create Labels and Entry Boxes for Row 1
        # add label and entry for the year
        self.year_label = tk.Label(self.entry_boxes_frame, text='Year')
        self.year_label.grid(row=1, column=0, sticky='e')

        self.year_spinbox = tk.Spinbox(self.entry_boxes_frame, from_=2003, to=2023)
        self.year_spinbox.grid(row=1, column=1, sticky='w')

        # add label and entry for the month
        self.month_label = tk.Label(self.entry_boxes_frame, text='Month')
        self.month_label.grid(row=1, column=2, sticky='e')

        self.month_spinbox = tk.Spinbox(self.entry_boxes_frame, from_=1, to=12)
        self.month_spinbox.grid(row=1, column=3, columnspan=3, sticky='w')

        # add label and entry for the client
        self.client_label = tk.Label(self.entry_boxes_frame, text='Client')
        self.client_label.grid(row=1, column=4, sticky='e')

        self.client_entry = tk.Entry(self.entry_boxes_frame)
        self.client_entry.grid(row=1, column=5, sticky='w')

        # Create Labels and Entry Boxes for Row 2

        # Create Label and Entry for Source Path
        self.source_path_label = tk.Label(self.entry_boxes_frame, text='Source \nPath')
        self.source_path_label.grid(row=2, column=0, sticky='e')

        self.source_path_entry = tk.Entry(self.entry_boxes_frame, width=55)
        self.source_path_entry.grid(row=2, column=1, columnspan=2)

        # Function to Select Source File
        def select_path(widget_name):
            source_name = tk.filedialog.askopenfilename(initialdir='/', title='Select a File',
                                                        filetypes=[('all files', '*.*'), ('Word', '*.docx')])
            widget_name.insert(0, source_name)

        # Button to Select Source File
        self.select_source_img = ImageTk.PhotoImage(Image.open('select_file_icon.png').resize((15, 15)))
        self.select_file_button = tk.Button(self.entry_boxes_frame, image=self.select_source_img,
                                            command=lambda: select_path(self.source_path_entry))
        self.select_file_button.grid(row=2, column=3, sticky='w')

        # Create Label and Entry for Target Path
        self.target_path_label = tk.Label(self.entry_boxes_frame, text='Target \nPath')
        self.target_path_label.grid(row=2, column=3, sticky='e')

        self.target_path_entry = tk.Entry(self.entry_boxes_frame, width=55)
        self.target_path_entry.grid(row=2, column=4, columnspan=2, sticky='w')

        # Button to Select Target File
        self.select_target_img = ImageTk.PhotoImage(Image.open('select_file_icon.png').resize((15, 15)))
        self.select_file_button = tk.Button(self.entry_boxes_frame, image=self.select_target_img,
                                            command=lambda: select_path(self.target_path_entry))
        self.select_file_button.grid(row=2, column=6, sticky='w')

        # Create Labels and Entry Boxes for Row 3

        # create label and entry for quantity
        self.quantity_label = tk.Label(self.entry_boxes_frame, text='Quantity')
        self.quantity_label.grid(row=3, column=0, sticky='e')

        self.quantity_entry = tk.Entry(self.entry_boxes_frame)
        self.quantity_entry.grid(row=3, column=1, sticky='w')

        # create label and entry for unit
        self.unit_label = tk.Label(self.entry_boxes_frame, text='Unit')
        self.unit_label.grid(row=3, column=2, sticky='e')

        self.unit_combobox = ttk.Combobox(self.entry_boxes_frame, values=['', 'chars', 'words', 'hours'])
        self.unit_combobox.grid(row=3, column=3, sticky='w')

        # add padding to all widgets within additional info frame:
        for widget in self.entry_boxes_frame.winfo_children():
            widget.grid_configure(padx=self.PAD_VALUE, pady=self.PAD_VALUE)

    def _create_controls_frame(self):
        pass

    def _create_control_buttons(self):
        pass
