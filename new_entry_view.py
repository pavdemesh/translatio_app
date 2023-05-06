import tkinter
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
from PIL import ImageTk, Image


class NewEntryWindow(tkinter.Toplevel):

    def __init__(self, controller):
        super().__init__()
        self.can_be_closed = False
        self.controller = controller
        self._new_entry_window()

    def _validate_submit_input_data(self):
        # Sanity Check Status first
        sanity_checked = self.sanity_status_var.get()
        if sanity_checked == 'Confirmed':
            # Translation Description
            tr_description = self.description_entry.get()
            # Subject
            tr_subject = self.subject_entry.get()
            # Source language
            tr_source_lang = self.source_lang_combobox.get()
            # Target language
            tr_target_lang = self.target_lang_combobox.get()
            if tr_description and tr_subject and tr_source_lang and tr_target_lang:
                # Year
                tr_year = self.year_spinbox.get() or 2023
                # Month
                tr_month = self.month_spinbox.get() or 5
                # Client
                tr_client = self.client_entry.get() or '-----'
                # Source Path
                tr_source_path = self.source_path_entry.get() or '-----'
                # Target path
                tr_target_path = self.target_path_entry.get() or '-----'
                # Quantity
                tr_quantity = self.quantity_entry.get() or 0
                # Unit
                tr_unit = self.unit_combobox.get() or '-----'
                # Store read data
                new_record_data = (tr_description, tr_subject, tr_source_lang, tr_target_lang, tr_year, tr_month,
                                   tr_client, tr_source_path, tr_target_path, tr_quantity, tr_unit)
                # Call Controller to Add New Record to Database
                self.controller.add_new_record(new_record_data)
                # Display successful submission message
                tkinter.messagebox.showinfo(title="Congrats!", message="Data successfully submitted!")
                # Set flag so that the window may be closed
                self.grab_release()
                self.quit()
                self.destroy()

            # If Description, Subject, Source Lang or Target Lang are missing
            else:
                tkinter.messagebox.showwarning(title='Error',
                                               message='Description, Subject and Languages are required')
        # If checkbox not checked
        else:
            tkinter.messagebox.showwarning(title='Confirmation Required',
                                           message='Please confirm that all data are correct')

    def _new_entry_window(self):
        # function to retrieve and submit all the data

        # add a title for the root self
        self.title('Translation Data Entry Form')

        # Make the Toplevel window be in Front of the Root
        self.grab_set()

        # create frame and pack it (place it)
        self.frame = tkinter.Frame(self)
        self.frame.pack()

        # create LabelFrame for basic translation info and fill it with widgets
        self.basic_info_frame = tkinter.LabelFrame(self.frame, text="Basic Translation Info")
        self.basic_info_frame.grid(row=0, column=0, padx=20, pady=10)

        # ----------------------- ROW 1 -----------------------

        # create data label (widget) and place it within first block
        self.description_label = tkinter.Label(self.basic_info_frame, text='Description')
        self.description_label.grid(row=0, column=0)

        self.description_entry = tkinter.Entry(self.basic_info_frame)
        self.description_entry.grid(row=1, column=0)

        # create data label (widget) and place it within first block
        self.subject_label = tkinter.Label(self.basic_info_frame, text='Subject')
        self.subject_label.grid(row=0, column=1)

        self.subject_entry = tkinter.Entry(self.basic_info_frame)
        self.subject_entry.grid(row=1, column=1)

        # create data label (widget) and place it within first block
        self.source_lang_label = tkinter.Label(self.basic_info_frame, text='Source Language')
        self.source_lang_label.grid(row=0, column=2)

        self.source_lang_combobox = ttk.Combobox(self.basic_info_frame, values=['', 'DE', 'EN', 'RU', 'UA'])
        self.source_lang_combobox.grid(row=1, column=2)

        # create data label (widget) and place it within first block
        self.target_lang_label = tkinter.Label(self.basic_info_frame, text='Target Language')
        self.target_lang_label.grid(row=0, column=3)

        self.target_lang_combobox = ttk.Combobox(self.basic_info_frame, values=['', 'DE', 'EN', 'RU', 'UA'])
        self.target_lang_combobox.grid(row=1, column=3)

        # ----------------------- ROW 2 -----------------------

        # add label for the second block - year
        self.year_label = tkinter.Label(self.basic_info_frame, text='Year')
        self.year_label.grid(row=2, column=0)

        self.year_spinbox = tkinter.Spinbox(self.basic_info_frame, from_=2003, to=2023)
        self.year_spinbox.grid(row=3, column=0)

        # add label for the second block - month
        self.month_label = tkinter.Label(self.basic_info_frame, text='Month')
        self.month_label.grid(row=2, column=1)

        self.month_spinbox = tkinter.Spinbox(self.basic_info_frame, from_=1, to=12)
        self.month_spinbox.grid(row=3, column=1)

        # add label for the second block - client
        self.client_label = tkinter.Label(self.basic_info_frame, text='Client')
        self.client_label.grid(row=2, column=2)

        self.client_entry = tkinter.Entry(self.basic_info_frame)
        self.client_entry.grid(row=3, column=2)

        # add padding to all widgets within basic info frame:
        for widget in self.basic_info_frame.winfo_children():
            widget.grid_configure(padx=10, pady=5)

        # create LabelFrame for additional translation info and fill it with widgets
        self.additional_info_frame = tkinter.LabelFrame(self.frame, text='Additional Translation Info')
        self.additional_info_frame.grid(row=1, column=0, sticky='news', padx=20, pady=10)

        # create label and entry form for source path
        self.source_path_label = tkinter.Label(self.additional_info_frame, text='Source Path')
        self.source_path_label.grid(row=0, column=0)

        self.source_path_entry = tkinter.Entry(self.additional_info_frame)
        self.source_path_entry.grid(row=1, column=0)

        def select_source_path():
            source_name = tkinter.filedialog.askopenfilename(initialdir='/', title='Select a File',
                                                             filetypes=[('all files', '*.*'), ('Word', '*.docx')])
            self.source_path_entry.insert(0, source_name)

        select_source_img = ImageTk.PhotoImage(Image.open('select_file_icon.png').resize((15, 15)))
        self.select_file_button = tkinter.Button(self.additional_info_frame, image=select_source_img,
                                                 command=select_source_path)
        self.select_file_button.grid(row=1, column=1)

        # create label and entry for target path
        self.target_path_label = tkinter.Label(self.additional_info_frame, text='Target Path')
        self.target_path_label.grid(row=0, column=2)

        self.target_path_entry = tkinter.Entry(self.additional_info_frame)
        self.target_path_entry.grid(row=1, column=2)

        def select_target_path():
            target_name = tkinter.filedialog.askopenfilename(initialdir='/', title='Select a File',
                                                             filetypes=[('all files', '*.*'), ('Word', '*.docx')])
            self.target_path_entry.insert(0, target_name)

        select_target_img = ImageTk.PhotoImage(Image.open('select_file_icon.png').resize((15, 15)))
        self.select_file_button = tkinter.Button(self.additional_info_frame, image=select_target_img,
                                                 command=select_target_path)
        self.select_file_button.grid(row=1, column=3)

        # create label and entry for quantity
        self.quantity_label = tkinter.Label(self.additional_info_frame, text='Quantity')
        self.quantity_label.grid(row=0, column=4)

        self.quantity_entry = tkinter.Entry(self.additional_info_frame)
        self.quantity_entry.grid(row=1, column=4)

        # create label and entry for unit
        self.unit_label = tkinter.Label(self.additional_info_frame, text='Unit')
        self.unit_label.grid(row=0, column=5)

        self.unit_combobox = ttk.Combobox(self.additional_info_frame, values=['', 'chars', 'words', 'hours'])
        self.unit_combobox.grid(row=1, column=5)

        # add padding to all widgets within additional info frame:
        for widget in self.additional_info_frame.winfo_children():
            widget.grid_configure(padx=10, pady=5)

        # Sanity check frame
        self.sanity_check_frame = tkinter.LabelFrame(self.frame, text='Sanity Check')
        self.sanity_check_frame.grid(row=2, column=0, sticky='news', padx=20, pady=10)

        self.sanity_status_var = tkinter.StringVar(value='Not Confirmed')
        self.sanity_checkbox = tkinter.Checkbutton(self.sanity_check_frame,
                                                   text='I checked the data entered: All fine!',
                                                   variable=self.sanity_status_var, onvalue='Confirmed',
                                                   offvalue='Not Confirmed')
        self.sanity_checkbox.grid(row=0, column=0)

        # create button to submit the data
        self.submit_button = tkinter.Button(self.frame, text='Submit data', command=self._validate_submit_input_data)
        self.submit_button.grid(row=3, column=0, sticky='new', padx=20, pady=10)

        # make the root self to be displayed
        self.mainloop()
