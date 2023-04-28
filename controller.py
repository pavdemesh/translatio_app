"""Controller Module for Translation Management App"""
from model import Model
from view import View


class Controller:
    """Controller for the Translation Database App"""
    # For its initialization the Controller object needs the objects of View and Model classes as parameters
    def __init__(self):
        self.model = Model()
        self.view = View(self)

    def main_start(self):
        self.view.main()

    def get_all_visible_records(self):
        return self.model.deliver_all_visible_records()

    def get_all_present_records(self):
        return self.model.deliver_all_present_records()

    def delete_row_by_id(self):
        row_id = self.view.deliver_selected_row_id()
        deletion_confirmation = self.view.display_deletion_confirmation()
        if deletion_confirmation == 'yes':
            self.model.mark_one_record_deleted_by_id(row_id)
        self.view.clear_treeview()
        self.view.clear_entry_boxes()
        self.view.display_content(self.get_all_visible_records())


if __name__ == "__main__":
    app_controller = Controller()
    app_controller.main_start()
