import tkinter
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
from PIL import ImageTk, Image
import tr_db_basic as trdb


def data_entry_window():
    # function to retrieve and submit all the data
    def submit_data():
        # Sanity Check Status first
        sanity_checked = sanity_status_var.get()
        if sanity_checked == 'Confirmed':
            # Translation Description
            tr_description = description_entry.get()
            # Subject
            tr_subject = subject_entry.get()
            # Source language
            tr_source_lang = source_lang_combobox.get()
            # Target language
            tr_target_lang = target_lang_combobox.get()
            if tr_description and tr_subject and tr_source_lang and tr_target_lang:
                # Year
                tr_year = year_spinbox.get()
                # Month
                tr_month = month_spinbox.get()
                # Client
                tr_client = client_entry.get()
                # Source Path
                tr_source_path = source_path_entry.get()
                # Target path
                tr_target_path = target_path_entry.get()
                # Quantity
                tr_quantity = quantity_entry.get()
                # Unit
                tr_unit = unit_combobox.get()
                connection = trdb.connect_db()
                with connection:
                    trdb.add_translation(connection, description=tr_description, subject=tr_subject,
                                         source_lang=tr_source_lang, target_lang=tr_target_lang, year=tr_year,
                                         month=tr_month, client=tr_client, source_path=tr_source_path,
                                         target_path=tr_target_path, quantity=tr_quantity, unit=tr_unit)
                window.destroy()
            else:
                tkinter.messagebox.showwarning(title='Error', message='Description, Subject and Languages are required')
        else:
            tkinter.messagebox.showwarning(title='Confirmation Required',
                                           message='Please confirm that all data are correct')

    # create a root window (where all the widgets and tabs will reside)
    window = tkinter.Toplevel()

    # add a title for the root window
    window.title('Translation Data Entry Form')

    # create frame and pack it (place it)
    frame = tkinter.Frame(window)
    frame.pack()

    # create LabelFrame for basic translation info and fill it with widgets
    basic_info_frame = tkinter.LabelFrame(frame, text="Basic Translation Info")
    basic_info_frame.grid(row=0, column=0, padx=20, pady=10)

    # ----------------------- ROW 1 -----------------------

    # create data label (widget) and place it within first block
    description_label = tkinter.Label(basic_info_frame, text='Description')
    description_label.grid(row=0, column=0)

    description_entry = tkinter.Entry(basic_info_frame)
    description_entry.grid(row=1, column=0)

    # create data label (widget) and place it within first block
    subject_label = tkinter.Label(basic_info_frame, text='Subject')
    subject_label.grid(row=0, column=1)

    subject_entry = tkinter.Entry(basic_info_frame)
    subject_entry.grid(row=1, column=1)

    # create data label (widget) and place it within first block
    source_lang_label = tkinter.Label(basic_info_frame, text='Source Language')
    source_lang_label.grid(row=0, column=2)

    source_lang_combobox = ttk.Combobox(basic_info_frame, values=['', 'DE', 'EN', 'RU', 'UA'])
    source_lang_combobox.grid(row=1, column=2)

    # create data label (widget) and place it within first block
    target_lang_label = tkinter.Label(basic_info_frame, text='Target Language')
    target_lang_label.grid(row=0, column=3)

    target_lang_combobox = ttk.Combobox(basic_info_frame, values=['', 'DE', 'EN', 'RU', 'UA'])
    target_lang_combobox.grid(row=1, column=3)

    # ----------------------- ROW 2 -----------------------

    # add label for the second block - year
    year_label = tkinter.Label(basic_info_frame, text='Year')
    year_label.grid(row=2, column=0)

    year_spinbox = tkinter.Spinbox(basic_info_frame, from_=2003, to=2023)
    year_spinbox.grid(row=3, column=0)

    # add label for the second block - month
    month_label = tkinter.Label(basic_info_frame, text='Month')
    month_label.grid(row=2, column=1)

    month_spinbox = tkinter.Spinbox(basic_info_frame, from_=1, to=12)
    month_spinbox.grid(row=3, column=1)

    # add label for the second block - client
    client_label = tkinter.Label(basic_info_frame, text='Client')
    client_label.grid(row=2, column=2)

    client_entry = tkinter.Entry(basic_info_frame)
    client_entry.grid(row=3, column=2)

    # add padding to all widgets within basic info frame:
    for widget in basic_info_frame.winfo_children():
        widget.grid_configure(padx=10, pady=5)

    # create LabelFrame for additional translation info and fill it with widgets
    additional_info_frame = tkinter.LabelFrame(frame, text='Additional Translation Info')
    additional_info_frame.grid(row=1, column=0, sticky='news', padx=20, pady=10)

    # create label and entry form for source path
    source_path_label = tkinter.Label(additional_info_frame, text='Source Path')
    source_path_label.grid(row=0, column=0)

    source_path_entry = tkinter.Entry(additional_info_frame)
    source_path_entry.grid(row=1, column=0)

    def select_source_path():
        source_name = tkinter.filedialog.askopenfilename(initialdir='/', title='Select a File',
                                                         filetypes=[('all files', '*.*'), ('Word', '*.docx')])
        source_path_entry.insert(0, source_name)

    select_source_img = ImageTk.PhotoImage(Image.open('select_file_icon.png').resize((15, 15)))
    select_file_button = tkinter.Button(additional_info_frame, image=select_source_img, command=select_source_path)
    select_file_button.grid(row=1, column=1)

    # create label and entry for target path
    target_path_label = tkinter.Label(additional_info_frame, text='Target Path')
    target_path_label.grid(row=0, column=2)

    target_path_entry = tkinter.Entry(additional_info_frame)
    target_path_entry.grid(row=1, column=2)

    def select_target_path():
        target_name = tkinter.filedialog.askopenfilename(initialdir='/', title='Select a File',
                                                         filetypes=[('all files', '*.*'), ('Word', '*.docx')])
        target_path_entry.insert(0, target_name)

    select_target_img = ImageTk.PhotoImage(Image.open('select_file_icon.png').resize((15, 15)))
    select_file_button = tkinter.Button(additional_info_frame, image=select_target_img, command=select_target_path)
    select_file_button.grid(row=1, column=3)

    # create label and entry for quantity
    quantity_label = tkinter.Label(additional_info_frame, text='Quantity')
    quantity_label.grid(row=0, column=4)

    quantity_entry = tkinter.Entry(additional_info_frame)
    quantity_entry.grid(row=1, column=4)

    # create label and entry for unit
    unit_label = tkinter.Label(additional_info_frame, text='Unit')
    unit_label.grid(row=0, column=5)

    unit_combobox = ttk.Combobox(additional_info_frame, values=['', 'chars', 'words', 'hours'])
    unit_combobox.grid(row=1,  column=5)

    # add padding to all widgets within additional info frame:
    for widget in additional_info_frame.winfo_children():
        widget.grid_configure(padx=10, pady=5)

    # Sanity check frame
    sanity_check_frame = tkinter.LabelFrame(frame, text='Sanity Check')
    sanity_check_frame.grid(row=2, column=0, sticky='news', padx=20, pady=10)

    sanity_status_var = tkinter.StringVar(value='Not Confirmed')
    sanity_checkbox = tkinter.Checkbutton(sanity_check_frame, text='I checked the data entered: All fine!',
                                          variable=sanity_status_var, onvalue='Confirmed', offvalue='Not Confirmed')
    sanity_checkbox.grid(row=0, column=0)

    # create button to submit the data
    submit_button = tkinter.Button(frame, text='Submit data', command=submit_data)
    submit_button.grid(row=3, column=0, sticky='new', padx=20, pady=10)

    # make the root window to be displayed
    window.mainloop()


# data_entry_window()
