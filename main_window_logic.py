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
        self.pushButton_delete_task_from_tree.setText("Удалить задачу")
        self.pushButton_delete_task.setText("Удалить задачу")
        self.label_tasks.setText("Задач нет")
        self.spinBox_task_priority.setMaximum(5)
        self.spinBox_task_priority.setMinimum(1)
        self.spinBox_task_priority.setValue(1)
        self.pushButton_save_task.clicked.connect(self.button_save_task_clicked)
        self.pushButton_delete_task_from_tree.clicked.connect(self.delete_task_using_tree_widget)
        self.pushButton_delete_task.clicked.connect(self.delete_task_using_input_fields)
        self.treeWidget.itemClicked.connect(self.item_clicked)
        self.treeWidget.setColumnCount(2)
        headers = ["Приоритет", "Название"]
        self.treeWidget.setHeaderLabels(headers)
        self.__current_item = None
        #Вот тут надо создать объект TaskManager


    def button_save_task_clicked(self):
        """Обработчик нажатия на кнопку "Cохранить задачу" """
        #Берем имя задачи из поля ввода
        task_name = self.lineEdit_task_name.text()
        #Берем приоритет задачи из поля ввода
        task_priority = self.spinBox_task_priority.text()
        #Очищаем поля ввода. Если не нужно, то можно удалить эти строчки
        self.lineEdit_task_name.clear()
        #Устанавливаем приоритет по умолчанию для задачи
        self.spinBox_task_priority.setValue(1)
        #Добавить задачу в вижет Дерево
        self.add_task_to_tree_widget(task_priority, task_name)
        #Вот тут надо добавить задачу в TaskManager
        #Также необходимо отрисовать задачи из TaskManager в label
        #self.label_tasks.setText(Сюда вставить строку с задачами)

    def add_task_to_tree_widget(self, priority: str, name: str):
        """Добавить задачу в виджет дерево
        priority: str - приоритет задачи
        name: str  - название задачи"""
        priority_item = self.__get_item_from_tree_widget(priority)
        if priority_item is None:
            priority_item = QTreeWidgetItem(self.treeWidget)
            priority_item.setText(0, priority)
        name_item = QTreeWidgetItem(priority_item)
        name_item.setText(1, name)

    def __get_item_from_tree_widget(self, text):
        for i in range(0, self.treeWidget.topLevelItemCount()):
            if self.treeWidget.topLevelItem(i).text(0) == text:
                return self.treeWidget.topLevelItem(i)
        return None

    def delete_task_using_input_fields(self):
        """Обработчик нажатия на кнопку "Удалить задачу" из label"""
        #Берем имя задачи из поля ввода
        task_name = self.lineEdit_task_name.text()
        #Берем приоритет задачи из поля ввода
        task_priority = self.spinBox_task_priority.text()
        #Очищаем поля ввода. Если не нужно, то можно удалить эти строчки
        self.lineEdit_task_name.clear()
        #Устанавливаем приоритет по умолчанию для задачи
        self.spinBox_task_priority.setValue(1)
        #Удаляем элемент из виджета дерево
        self.__current_item = self.__get_item_by_priority_and_name(task_priority, task_name)
        self.delete_item_from_tree_widget()
        #Удалить задачу из TaskManager
        #Заново отрисовать задачи в label
        #self.label_tasks.setText(Сюда вставить строку с задачами)

    def __get_item_by_priority_and_name(self, priority, name):
        item:QTreeWidgetItem = self.__get_item_from_tree_widget(priority)
        if item is None:
            return
        for i in range(0, item.childCount()):
            if item.child(i).text(1) == name:
                return item.child(i)
        return None

    def delete_task_using_tree_widget(self):
        """Обработчик нажатия на кнопку "Удалить задачу" из виджета дерева"""
        priority = self.__get_priority_from_tree_widget()
        if priority is None:
            return
        name = self.__get_name_from_tree_widget()
        if name is None:
            return
        self.delete_item_from_tree_widget()
        #Удалить задачу из TaskManager
        #Заново отрисовать задачи в label
        #self.label_tasks.setText(Сюда вставить строку с задачами)

    def delete_item_from_tree_widget(self):
        if self.__current_item is None:
            return
        parent:QTreeWidgetItem = self.__current_item.parent()
        if parent is None:
            return
        parent.removeChild(self.__current_item)
        if parent.childCount() == 0:
            parent.removeChild(parent)

    def __get_priority_from_tree_widget(self):
        if self.__current_item is None:
            return None
        parent:QTreeWidgetItem = self.__current_item.parent()
        if parent is None:
            return None
        return parent.text(0)

    def __get_name_from_tree_widget(self):
        if self.__current_item is None:
            return None
        parent:QTreeWidgetItem = self.__current_item.parent()
        if parent is None:
            return
        return self.__current_item.text(1)

    def item_clicked(self, item, column):
        """Обработчик выбора элемента в виджете дерево"""
        self.__current_item = item
