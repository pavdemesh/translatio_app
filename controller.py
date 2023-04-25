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


if __name__ == "__main__":
    app_controller = Controller()
    app_controller.main_start()
