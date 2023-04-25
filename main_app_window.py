import tkinter
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
import data_entry_interface
import sqlite3

from PIL import ImageTk, Image

window = tkinter.Tk()
window.title("Translation Database Viewer App")
window.geometry('1200x700')

# Customize Style
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

# Create Frame for Viewer
frame_for_tree = tkinter.Frame(window)
frame_for_tree.pack(pady=10)

# Create a Treeview Scrollbar
scroll_tree = tkinter.Scrollbar(frame_for_tree)
scroll_tree.pack(side="right", fill="y")

# Create a Treeview
data_tree = ttk.Treeview(frame_for_tree, yscrollcommand=scroll_tree.set, selectmode='extended')
data_tree.pack()

# Configure the Scrollbar
scroll_tree.configure(command=data_tree.yview)

# Define Columns
data_tree['columns'] = ("ID", "Description", "Subject", "Source Lang", "Target Lang",
                        "Year", "Month", "Client", "Source File", "Target File", "Quantity", "Unit")

# Format Columns
data_tree.column("#0", width=0, stretch=False)
data_tree.column("ID", anchor='center', width=40, minwidth=25)
data_tree.column("Description", anchor='w', width=140, minwidth=50)
data_tree.column("Subject", anchor='w', width=140, minwidth=50)
data_tree.column("Source Lang", anchor='center', width=70, minwidth=35)
data_tree.column("Target Lang", anchor='center', width=70, minwidth=35)
data_tree.column("Year", anchor='center', width=50, minwidth=35)
data_tree.column("Month", anchor='center', width=50, minwidth=35)
data_tree.column("Client", anchor='center', width=140, minwidth=50)
data_tree.column("Source File", anchor='w', width=140, minwidth=50)
data_tree.column("Target File", anchor='w', width=140, minwidth=50)
data_tree.column("Quantity", anchor='center', width=60, minwidth=35)
data_tree.column("Unit", anchor='center', width=60, minwidth=35)

# Create Headings
data_tree.heading("#0", text="", anchor='center')
data_tree.heading("ID", text="ID", anchor='center')
data_tree.heading("Description", text="Description", anchor='center')
data_tree.heading("Subject", text="Subject", anchor='center')
data_tree.heading("Source Lang", text="Source Lang", anchor='center')
data_tree.heading("Target Lang", text="Target Lang", anchor='center')
data_tree.heading("Year", text="Year", anchor='center')
data_tree.heading("Month", text="Month", anchor='center')
data_tree.heading("Client", text="Client", anchor='center')
data_tree.heading("Source File", text="Source File", anchor='center')
data_tree.heading("Target File", text="Target File", anchor='center')
data_tree.heading("Quantity", text="Quantity", anchor='center')
data_tree.heading("Unit", text="Unit", anchor='center')

# Configure Color for Odd and Even Rows
data_tree.tag_configure('oddrow', background='white')
data_tree.tag_configure('evenrow', background='lightblue')

# Connect to the Database
connection = sqlite3.connect('translations.db')

# Import Data From Database into Treeview
with connection:
    # Get all records from database as a  list of tuples

    database_records = connection.execute('SELECT rowid, * FROM translatio').fetchall()
    # Iterate through the list of tuples = content of the database
    # Crete counter to account for even and odd rows
    count = 0
    for record in database_records:
        # If the row count is even:
        if count % 2 == 0:
            # Insert data with even row tag
            data_tree.insert(parent='', index='end', text='',
                             values=(record[0], record[1], record[2], record[3], record[4], record[5], record[6],
                                     record[7], record[8], record[9], record[10], record[11]), tags=['evenrow'])
        # If the row count is odd
        if count % 2 == 1:
            data_tree.insert(parent='', index='end', text='',
                             values=(record[0], record[1], record[2], record[3], record[4], record[5], record[6],
                                     record[7], record[8], record[9], record[10]), tags=['oddrow'])
        # Increase counter by 1
        count += 1

# Create Frame for Entry Boxes and Button Controls
frame_for_boxes = tkinter.LabelFrame(window, text="Modify Data Fields")
frame_for_boxes.pack()

# Add Entry Boxes to be Filled by Data in Selected Row

# Create Labels and Entry Boxes for Row 0
description_label = tkinter.Label(frame_for_boxes, text='Description')
description_label.grid(row=0, column=0, sticky='e')

description_entry = tkinter.Entry(frame_for_boxes, width=30)
description_entry.grid(row=0, column=1, sticky='w')

# create data label (widget) and place it within first block
subject_label = tkinter.Label(frame_for_boxes, text='Subject')
subject_label.grid(row=0, column=2, sticky='e')

subject_entry = tkinter.Entry(frame_for_boxes, width=30)
subject_entry.grid(row=0, column=3, sticky='w')

# create data label (widget) and place it within first block
source_lang_label = tkinter.Label(frame_for_boxes, text='Source \nLanguage')
source_lang_label.grid(row=0, column=4, sticky='e')

source_lang_combobox = ttk.Combobox(frame_for_boxes, values=['', 'DE', 'EN', 'RU', 'UA'], width=15)
source_lang_combobox.grid(row=0, column=5, sticky='w')

# create data label (widget) and place it within first block
target_lang_label = tkinter.Label(frame_for_boxes, text='Target \nLanguage')
target_lang_label.grid(row=0, column=6, sticky='w')

target_lang_combobox = ttk.Combobox(frame_for_boxes, values=['', 'DE', 'EN', 'RU', 'UA'], width=15)
target_lang_combobox.grid(row=0, column=7, sticky='w')

# Create Labels and Entry Boxes for Row 1

# add label and entry for the year
year_label = tkinter.Label(frame_for_boxes, text='Year')
year_label.grid(row=1, column=0, sticky='e')

year_spinbox = tkinter.Spinbox(frame_for_boxes, from_=2003, to=2023)
year_spinbox.grid(row=1, column=1, sticky='w')

# add label and entry for the month
month_label = tkinter.Label(frame_for_boxes, text='Month')
month_label.grid(row=1, column=2, sticky='e')

month_spinbox = tkinter.Spinbox(frame_for_boxes, from_=1, to=12)
month_spinbox.grid(row=1, column=3, columnspan=3, sticky='w')

# add label and entry for the client
client_label = tkinter.Label(frame_for_boxes, text='Client')
client_label.grid(row=1, column=4, sticky='e')

client_entry = tkinter.Entry(frame_for_boxes)
client_entry.grid(row=1, column=5, sticky='w')

# add padding to all widgets within basic info frame:
for widget in frame_for_boxes.winfo_children():
    widget.grid_configure(padx=5, pady=5)

# Create Labels and Entry Boxes for Row 2

# Create Label and Entry for Source Path
source_path_label = tkinter.Label(frame_for_boxes, text='Source \nPath')
source_path_label.grid(row=2, column=0, sticky='e')

source_path_entry = tkinter.Entry(frame_for_boxes, width=55)
source_path_entry.grid(row=2, column=1, columnspan=2)


# Function to Select Source File
def select_source_path():
    source_name = tkinter.filedialog.askopenfilename(initialdir='/', title='Select a File',
                                                     filetypes=[('all files', '*.*'), ('Word', '*.docx')])
    source_path_entry.insert(0, source_name)


# Button to Select Source File
select_source_img = ImageTk.PhotoImage(Image.open('select_file_icon.png').resize((15, 15)))
select_file_button = tkinter.Button(frame_for_boxes, image=select_source_img, command=select_source_path)
select_file_button.grid(row=2, column=3, sticky='w')

# Create Label and Entry for Target Path
target_path_label = tkinter.Label(frame_for_boxes, text='Target \nPath')
target_path_label.grid(row=2, column=3, sticky='e')

target_path_entry = tkinter.Entry(frame_for_boxes, width=55)
target_path_entry.grid(row=2, column=4, columnspan=2, sticky='w')


# Function to Select Target File
def select_target_path():
    target_name = tkinter.filedialog.askopenfilename(initialdir='/', title='Select a File',
                                                     filetypes=[('all files', '*.*'), ('Word', '*.docx')])
    target_path_entry.insert(0, target_name)


# Button to Select Target File
select_target_img = ImageTk.PhotoImage(Image.open('select_file_icon.png').resize((15, 15)))
select_file_button = tkinter.Button(frame_for_boxes, image=select_target_img, command=select_target_path)
select_file_button.grid(row=2, column=6, sticky='w')

# Create Labels and Entry Boxes for Row 3

# create label and entry for quantity
quantity_label = tkinter.Label(frame_for_boxes, text='Quantity')
quantity_label.grid(row=3, column=0, sticky='e')

quantity_entry = tkinter.Entry(frame_for_boxes)
quantity_entry.grid(row=3, column=1, sticky='w')

# create label and entry for unit
unit_label = tkinter.Label(frame_for_boxes, text='Unit')
unit_label.grid(row=3, column=2, sticky='e')

unit_combobox = ttk.Combobox(frame_for_boxes, values=['', 'chars', 'words', 'hours'])
unit_combobox.grid(row=3, column=3, sticky='w')

# add padding to all widgets within additional info frame:
for widget in frame_for_boxes.winfo_children():
    widget.grid_configure(padx=10, pady=5)

# Create Frame for Buttons
frame_for_controls = tkinter.LabelFrame(window, text="Database Controls")
frame_for_controls.pack()


# Define Functions to be Used in COMMAND argument in Buttons

# Function to Add a New Entry (opens a new window)
def add_new_record():
    data_entry_interface.data_entry_window()


# Function to Delete Selected Record
def delete_one_record():
    selected_row = data_tree.selection()[0]
    row_id = data_tree.item(selected_row)['values'][0]
    print(row_id)
    print(type(row_id))
    deletion_confirmation = tkinter.messagebox.askquestion(title='Are you sure?',
                                                message='Deletion of can not be undone.\n Do you wish to continue?',
                                                icon='warning')
    if deletion_confirmation == 'yes':
        tkinter.messagebox.showinfo(title="Hui tebe, kozhanyi ubliudok", message='You have no power here')
    else:
        tkinter.messagebox.showinfo(title='Zassal?', message='Realno zassal :-)')


# Delete Many Selected Records
def delete_many_selected():
    pass


# Function to Delete All Records
def delete_all_records():
    """Not Really Needed"""
    pass


# Function to Update Selected Record
def update_record():
    pass


# Function to Clear the Entry Boxes
def clear_entry_boxes():
    for widget in frame_for_boxes.winfo_children():
        if widget.winfo_class() in ['Entry', 'Spinbox', 'TCombobox']:
            widget.delete(0, 'end')


# Function to Clear Entry Boxes without Updating Record
def select_record(e):
    # Clear Entry Boxes First
    for widget in frame_for_boxes.winfo_children():
        if widget.winfo_class() in ['Entry', 'Spinbox', 'TCombobox']:
            widget.delete(0, 'end')

    # Grab Record Number
    selected = data_tree.focus()
    # Grab Record Values
    selected_values = data_tree.item(selected, "values")

    # Insert Values Into Entry Fields
    value_index = 0
    for widget in frame_for_boxes.winfo_children():
        if widget.winfo_class() in ['Entry', 'Spinbox', 'TCombobox']:
            widget.insert(0, selected_values[value_index])
            value_index += 1


# Bind Left Mouse Click to Select a Record
data_tree.bind('<ButtonRelease-1>', select_record)


# Function to Move the Record Up
def move_record_up():
    """Not Really Needed"""
    pass


# Function to Move the Record Down
def move_record_down():
    """Not Really Needed"""
    pass


# Create a Button to Add a New Record to the Database and Update the Treeview and Table
add_new_record_btn = tkinter.Button(frame_for_controls, text="Add New Record", command=add_new_record)
add_new_record_btn.grid(row=0, column=0, padx=10, pady=10)

# Create a Button to Update Selected Record and Update the Treeview and Table
update_record_btn = tkinter.Button(frame_for_controls, text="Update Record", command=update_record)
update_record_btn.grid(row=0, column=1, padx=10, pady=10)

# Create a Button to Delete Selected Record and Update the Treeview and Table
delete_one_record_btn = tkinter.Button(frame_for_controls, text="Delete Record", command=delete_one_record)
delete_one_record_btn.grid(row=0, column=2, padx=10, pady=10)

# Create a Button to Delete Many Selected Records and Update the Treeview and Table
delete_many_records_btn = tkinter.Button(frame_for_controls,
                                         text="Delete Selected Records", command=delete_many_selected)
delete_many_records_btn.grid(row=0, column=3, padx=10, pady=10)

# Create a Button to Delete All Records and Update the Treeview and Table
delete_all_records_btn = tkinter.Button(frame_for_controls, text="Delete All Records", command=delete_all_records)
delete_all_records_btn.grid(row=0, column=4, padx=10, pady=10)

# Create a Button to Move Up Selected Record and Update the Treeview and Table
move_up_record_btn = tkinter.Button(frame_for_controls, text="Move Up Record", command=move_record_up)
move_up_record_btn.grid(row=0, column=5, padx=10, pady=10)

# Create a Button to Move Down Selected Record and Update the Treeview and Table
move_down_record_btn = tkinter.Button(frame_for_controls, text="Move Down Record", command=move_record_down)
move_down_record_btn.grid(row=0, column=6, padx=10, pady=10)

# Create a Button to Clear the Entry Boxes
clear_entry_boxes_btn = tkinter.Button(frame_for_controls, text="Clear Entry Boxes", command=clear_entry_boxes)
clear_entry_boxes_btn.grid(row=0, column=7, padx=10, pady=10)

window.mainloop()
