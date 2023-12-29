from abc import ABCMeta, abstractmethod


class MainWindowView(metaclass = ABCMeta):

    @abstractmethod
    def get_task_name_text(self) -> str:
        pass

    @abstractmethod
    def get_task_priority_text(self) -> str:
        pass

    @abstractmethod
    def clear_all_input_fields(self) -> None:
        pass

    @abstractmethod
    def add_task_to_tree_widget(self, priority: str, name: str):
        pass

    @abstractmethod
    def get_tree_item_by_priority_and_name(self, priority, name):
        pass

    @abstractmethod
    def delete_item_from_tree_widget(self, item):
        pass

    @abstractmethod
    def get_name_from_tree_widget(self, item):
        pass

    @abstractmethod
    def get_priority_from_tree_widget(self, item):
        pass
