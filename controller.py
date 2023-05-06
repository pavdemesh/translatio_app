"""Controller Module for Translation Management App"""
from model import Model
from view import View


class Controller:
    """Controller for the Translation Database App"""
    # For its initialization the Controller object needs the objects of View and Model classes as parameters
    def __init__(self):
        self.new_record_window = None
        self.model = Model()
        self.view = View(self)

    def main_start(self):
        self.view.main()

    def get_all_visible_records(self):
        return self.model.deliver_all_visible_records()

    # Requesst all visible records from Model and return a list of tuples
    def get_all_present_records(self):
        return self.model.deliver_all_present_records()

    # Delete a Single Row by id
    def delete_row_by_id(self):
        # Get row_id from selected row
        row_id = self.view.deliver_selected_row_id()
        # Ask for deletion confirmation
        deletion_confirmation = self.view.display_deletion_confirmation()
        if deletion_confirmation == 'yes':
            # Mark record in database (Model) as deleted
            self.model.mark_one_record_deleted_by_id(row_id)
        # Clear Treeview, Clear Entry Boxes and Display Updated Treeview
        self.view.update_treeview()

    # Function to add new entry to the database (Model), require data - a tuple
    def add_new_record(self, data):
        self.model.add_record_to_table(data)


if __name__ == "__main__":
    app_controller = Controller()
    app_controller.main_start()
