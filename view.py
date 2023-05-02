"""View Module for Translation Management App"""

import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
from tkinter import font
from PIL import ImageTk, Image
from new_entry_view import NewEntryWindow


class View(tk.Tk):
    """This Class handles the representation of data"""
    """
    self.treeview_frame
    self.treeview_scroll
    self.data_treeview
    """
    # Size of Padding
    PAD_VALUE_BIG = 10
    PAD_VALUE_SMALL = 5

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
        # Configure display of deleted rows
        self._configure_display_of_deleted_rows()
        # Create Frame for Entry Boxes and Labels
        self._create_entry_boxes_frame()
        # Create Entry Boxes in the Entry Frame
        self._create_entry_boxes()
        # Create Frame for Button Controls
        self._create_controls_frame()
        # Create Controls
        self._create_control_buttons()
        # Display Content of the Database
        self.display_content(self.controller.get_all_visible_records())
        # Configure Behaviour on Left Mouse Click
        self._define_left_mouseclick()

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
        self.treeview_frame.pack(padx=self.PAD_VALUE_BIG, pady=self.PAD_VALUE_BIG)

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

    def _configure_display_of_deleted_rows(self):
        # Get parameters of the default font as a dictionary
        default_font_params = font.nametofont("TkDefaultFont").actual()
        # Create a copy of the default font, but ith overstrike activated
        my_font = font.Font(family=default_font_params['family'],
                            size=default_font_params['size'],
                            weight=default_font_params['weight'],
                            slant=default_font_params['slant'],
                            underline=default_font_params['underline'],
                            overstrike=True)
        self.data_treeview.tag_configure('is_deleted', font=my_font)

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
            widget.grid_configure(padx=self.PAD_VALUE_SMALL, pady=self.PAD_VALUE_SMALL)

    def _create_controls_frame(self):
        self.controls_frame = tk.LabelFrame(self, text="Control Buttons")
        self.controls_frame.pack()

    def _create_control_buttons(self):
        # Create a Button to Add a New Record to the Database and Update the Treeview and Table
        self.add_new_record_btn = tk.Button(self.controls_frame, text="Add New Record",
                                            command=self._add_new_entry)
        self.add_new_record_btn.grid(row=0, column=0, padx=10, pady=10)

        # Create a Button to Update Selected Record and Update the Treeview and Table
        self.update_record_btn = tk.Button(self.controls_frame, text="Update Record")
        self.update_record_btn.grid(row=0, column=1, padx=10, pady=10)

        # Create a Button to Delete Selected Record and Update the Treeview and Table
        self.delete_one_record_btn = tk.Button(self.controls_frame,
                                               text="Delete Record", command=self.controller.delete_row_by_id)
        self.delete_one_record_btn.grid(row=0, column=2, padx=10, pady=10)

        # Create a Button to Delete Many Selected Records and Update the Treeview and Table
        self.delete_many_records_btn = tk.Button(self.controls_frame, text="Delete Selected Records")
        self.delete_many_records_btn.grid(row=0, column=3, padx=10, pady=10)

        # Create a Button to Delete All Records and Update the Treeview and Table
        self.delete_all_records_btn = tk.Button(self.controls_frame, text="Delete All Records")
        self.delete_all_records_btn.grid(row=0, column=4, padx=10, pady=10)

        # Create a Button to Move Up Selected Record and Update the Treeview and Table
        self.move_up_record_btn = tk.Button(self.controls_frame, text="Move Up Record")
        self.move_up_record_btn.grid(row=0, column=5, padx=10, pady=10)

        # Create a Button to Move Down Selected Record and Update the Treeview and Table
        self.clear_treeview_btn = tk.Button(self.controls_frame, text="Clear Treeview", command=self.clear_treeview)
        self.clear_treeview_btn.grid(row=0, column=6, padx=10, pady=10)

        # Create a Button to Clear the Entry Boxes
        self.clear_entry_boxes_btn = tk.Button(self.controls_frame,
                                               text="Clear Entry Boxes", command=self.clear_entry_boxes)
        self.clear_entry_boxes_btn.grid(row=0, column=7, padx=10, pady=10)

    def display_content(self, database_records: list[tuple]):
        # Iterate through the list of tuples = content of the database
        # Crete counter to account for even and odd rows
        count = 0
        for record in database_records:
            # If the row count is even:
            if count % 2 == 0 and record[12] == 0:
                # Insert data with even row tag
                self.data_treeview.insert(parent='', index='end', text='',
                                          values=(record[0], record[1], record[2], record[3], record[4], record[5],
                                                  record[6], record[7], record[8], record[9], record[10],
                                                  record[11]),
                                          tags=['evenrow'])

            elif count % 2 == 0 and record[12] == 1:
                # Insert data with even row tag
                self.data_treeview.insert(parent='', index='end', text='',
                                          values=(record[0], record[1], record[2], record[3], record[4], record[5],
                                                  record[6], record[7], record[8], record[9], record[10],record[11]),
                                          tags=['evenrow', 'is_deleted'])

            # If the row count is odd
            elif count % 2 == 1 and record[12] == 0:
                self.data_treeview.insert(parent='', index='end', text='',
                                          values=(record[0], record[1], record[2], record[3], record[4], record[5],
                                                  record[6], record[7], record[8], record[9], record[10], record[11]),
                                          tags=['oddrow'])

            elif count % 2 == 1 and record[12] == 1:
                self.data_treeview.insert(parent='', index='end', text='',
                                          values=(record[0], record[1], record[2], record[3], record[4], record[5],
                                                  record[6], record[7], record[8], record[9], record[10], record[11]),
                                          tags=['oddrow', 'is_deleted'])
            # Increase counter by 1
            count += 1

    def display_deletion_confirmation(self):
        return tk.messagebox.askquestion(title='Are you sure you want to delete the record(s)?',
                                         message='Deletion can not be undone.\n Continue?', icon='warning')

    def clear_entry_boxes(self):
        # Clear Entry Boxes First
        for widget in self.entry_boxes_frame.winfo_children():
            if widget.winfo_class() in ['Entry', 'Spinbox', 'TCombobox']:
                widget.delete(0, 'end')

    def clear_treeview(self):
        for item in self.data_treeview.get_children():
            self.data_treeview.delete(item)

    def _select_record(self, e):
        # Clear Entry Boxes First
        self.clear_entry_boxes()
        # Grab Record Number
        selected = self.data_treeview.focus()
        # Grab Record Values
        selected_values = self.data_treeview.item(selected, "values")

        # Insert Values Into Entry Fields Omitting the 0-st index (row_id)
        value_index = 1
        for widget in self.entry_boxes_frame.winfo_children():
            if widget.winfo_class() in ['Entry', 'Spinbox', 'TCombobox']:
                widget.insert(0, selected_values[value_index])
                value_index += 1
                print(value_index)
        # Return the RID of the selected row

    def deliver_selected_row_id(self):
        # Grab Record Number
        selected = self.data_treeview.focus()
        # Grab Record Values
        selected_values = self.data_treeview.item(selected, "values")
        # Return the RID of the selected row - index 0
        return selected_values[0]

    def _define_left_mouseclick(self):
        # Bind Left Mouse Click to Select a Record
        self.data_treeview.bind('<ButtonRelease-1>', self._select_record)

    def update_treeview(self):
        # Clear Treeview
        self.clear_treeview()
        # Clear Entry Boxes
        self.clear_entry_boxes()
        # Display Updated Treeview
        self.display_content(self.controller.get_all_visible_records())

    def _add_new_entry(self):
        # Show entry window
        new_window = NewEntryWindow()
        # Get data from the entry form
        new_data = new_window.new_record_data
        # If data really present - add them to the table
        if new_data:
            self.controller.add_new_record(new_data)
        # Update the treeview
        # self.update_treeview()
        # self.clear_treeview()

