from PyQt5.QtWidgets import QMainWindow, QTreeWidgetItem

from main_window import Ui_MainWindow


class MainWindowLogic(QMainWindow, Ui_MainWindow):

    def __init__(self, *args, **kwargs):
        QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        self.show()

        self.label_task_name.setText("Название задачи")
        self.label_task_priority.setText("Приоритет задачи")
        self.pushButton_save_task.setText("Сохранить задачу")
        self.pushButton_delete_task.setText("Удалить задачу")
        self.spinBox_task_priority.setMaximum(5)
        self.spinBox_task_priority.setMinimum(1)
        self.spinBox_task_priority.setValue(1)
        self.pushButton_save_task.clicked.connect(self.button_save_task_clicked)
        self.pushButton_delete_task.clicked.connect(self.delete_task_from_tree_widget)
        self.treeWidget.itemClicked.connect(self.item_clicked)
        self.treeWidget.setColumnCount(2)
        headers = ["Приоритет", "Название"]
        self.treeWidget.setHeaderLabels(headers)
        self.current_item = None
        self.current_column = -1


    def button_save_task_clicked(self):
        task_name = self.lineEdit_task_name.text()
        task_priority = self.spinBox_task_priority.text()
        self.lineEdit_task_name.clear()
        self.spinBox_task_priority.setValue(1)
        self.add_task_to_tree_widget(task_priority, task_name)

    def add_task_to_tree_widget(self, priority: str, name: str):
        priority_item = self.get_item_from_tree_widget(priority)
        if priority_item is None:
            priority_item = QTreeWidgetItem(self.treeWidget)
            priority_item.setText(0, priority)
        name_item = QTreeWidgetItem(priority_item)
        name_item.setText(1, name)

    def get_item_from_tree_widget(self, text):
        for i in range(0, self.treeWidget.topLevelItemCount()):
            if self.treeWidget.topLevelItem(i).text(0) == text:
                return self.treeWidget.topLevelItem(i)
        return None

    def delete_task_from_tree_widget(self):
        if self.current_item is None:
            return
        parent:QTreeWidgetItem = self.current_item.parent()
        parent.removeChild(self.current_item)
        if parent.childCount() == 0:
            parent.removeChild(parent)

    def item_clicked(self, item, column):
        self.current_item = item
        self.current_column = column
