from collections import defaultdict
from Stack import Stack


class StackManager:
    def __init__(self):
        self.__stack = defaultdict(Stack)

    def add(self, elem, priority):
        self.__stack[priority].add(elem)
        print('Задача добавлена.')

    def delete_priority(self, priority):
        if self.__stack[priority].is_empty():
            del self.__stack[priority]

    def delete_elem(self, elem, priority):
        if priority in self.__stack:
            if elem in self.__stack[priority].get_stack():
                self.__stack[priority].delete_elem(elem)
                print('Задача удалена.')
                self.delete_priority(priority)
            else:
                print('Такой задачи с выбранным приоритетом нет.')
        else:
            print('Такой задачи с выбранным приоритетом нет.')

    def print_tasks(self):
        if len(self.__stack) == 0:
            print('Список пустой.')
        else:
            for priority_index, tasks in sorted(self.__stack.items()):
                print(priority_index, tasks)

    def __str__(self):
        string = ''
        if len(self.__stack) == 0:
            return 'Список пустой.'
        else:
            for priority_index, tasks in sorted(self.__stack.items()):
                string += priority_index + ' ' + str(tasks) + '\n'
        return string