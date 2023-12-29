from main_window_view import MainWindowView


class MainWindowPresenter:
    def __init__(self, view):
        self.__view:MainWindowView = view
        self.__current_tree_item = None

    def button_save_clicked(self):
        task_name = self.__view.get_task_name_text()
        task_priority = self.__view.get_task_priority_text()
        self.__view.clear_all_input_fields()
        self.__view.add_task_to_tree_widget(task_priority, task_name)

    def button_delete_using_inputs_clicked(self):
        task_name = self.__view.get_task_name_text()
        task_priority = self.__view.get_task_priority_text()
        self.__view.clear_all_input_fields()
        item = self.__view.get_tree_item_by_priority_and_name(task_priority, task_name)
        self.__view.delete_item_from_tree_widget(item)

    def button_delete_task_using_tree_widget_clicked(self):
        task_name = self.__view.get_name_from_tree_widget(self.__current_tree_item)
        task_priorit = self.__view.get_priority_from_tree_widget(self.__current_tree_item)
        self.__view.delete_item_from_tree_widget(self.__current_tree_item)

    def tree_item_clicked(self, item):
        self.__current_tree_item = item
