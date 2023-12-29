from PyQt5.QtWidgets import QMainWindow, QTreeWidgetItem

from main_window import Ui_MainWindow
from main_window_meta import MainWindowMeta
from main_window_presenter import MainWindowPresenter
from main_window_view import MainWindowView


class MainWindowLogic(QMainWindow, MainWindowView, metaclass = MainWindowMeta):

    def __init__(self, parent = None):
        super(QMainWindow, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.show()

        self.ui.label_task_name.setText("Название задачи")
        self.ui.label_task_priority.setText("Приоритет задачи")
        self.ui.pushButton_save_task.setText("Сохранить задачу")
        self.ui.pushButton_delete_task_from_tree.setText("Удалить задачу")
        self.ui.pushButton_delete_task.setText("Удалить задачу")
        self.ui.label_tasks.setText("Задач нет")
        self.ui.spinBox_task_priority.setMaximum(5)
        self.ui.spinBox_task_priority.setMinimum(1)
        self.ui.spinBox_task_priority.setValue(1)
        self.ui.pushButton_save_task.clicked.connect(self.button_save_task_clicked)
        self.ui.pushButton_delete_task_from_tree.clicked.connect(self.delete_task_using_tree_widget)
        self.ui.pushButton_delete_task.clicked.connect(self.delete_task_using_input_fields)
        self.ui.treeWidget.itemClicked.connect(self.item_clicked)
        self.ui.treeWidget.setColumnCount(2)
        headers = ["Приоритет", "Название"]
        self.ui.treeWidget.setHeaderLabels(headers)
        self.__presenter: MainWindowPresenter = MainWindowPresenter(self)


    def button_save_task_clicked(self):
        """Обработчик нажатия на кнопку "Cохранить задачу" """
        self.__presenter.button_save_clicked()

    def get_task_name_text(self) -> str:
        return self.ui.lineEdit_task_name.text()

    def get_task_priority_text(self) -> str:
        return self.ui.spinBox_task_priority.text()

    def clear_all_input_fields(self) -> None:
        self.ui.spinBox_task_priority.setValue(1)
        self.ui.lineEdit_task_name.clear()

    def add_task_to_tree_widget(self, priority: str, name: str):
        """Добавить задачу в виджет дерево
        priority: str - приоритет задачи
        name: str  - название задачи"""
        priority_item = self.__get_item_from_tree_widget(priority)
        if priority_item is None:
            priority_item = QTreeWidgetItem(self.ui.treeWidget)
            priority_item.setText(0, priority)
        name_item = QTreeWidgetItem(priority_item)
        name_item.setText(1, name)

    def __get_item_from_tree_widget(self, text):
        for i in range(0, self.ui.treeWidget.topLevelItemCount()):
            if self.ui.treeWidget.topLevelItem(i).text(0) == text:
                return self.ui.treeWidget.topLevelItem(i)
        return None

    def delete_task_using_input_fields(self):
        """Обработчик нажатия на кнопку "Удалить задачу" из label"""
        self.__presenter.button_delete_using_inputs_clicked()

    def get_tree_item_by_priority_and_name(self, priority, name):
        item:QTreeWidgetItem = self.__get_item_from_tree_widget(priority)
        if item is None:
            return
        for i in range(0, item.childCount()):
            if item.child(i).text(1) == name:
                return item.child(i)
        return None

    def delete_task_using_tree_widget(self):
        """Обработчик нажатия на кнопку "Удалить задачу" из виджета дерева"""
        self.__presenter.button_delete_task_using_tree_widget_clicked()


    def delete_item_from_tree_widget(self, item):
        if item is None:
            return
        parent:QTreeWidgetItem = item.parent()
        if parent is None:
            return
        parent.removeChild(item)
        if parent.childCount() == 0:
            parent.removeChild(parent)

    def get_priority_from_tree_widget(self, item):
        if item is None:
            return None
        parent:QTreeWidgetItem = item.parent()
        if parent is None:
            return None
        return parent.text(0)

    def get_name_from_tree_widget(self, item):
        if item is None:
            return None
        parent:QTreeWidgetItem = item.parent()
        if parent is None:
            return
        return item.text(1)

    def item_clicked(self, item, column):
        """Обработчик выбора элемента в виджете дерево"""
        self.__presenter.tree_item_clicked(item)
