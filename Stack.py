class Stack:
    def __init__(self):
        self.__stack = list()

    def get_stack(self):
        return self.__stack

    def add(self, elem):
        self.__stack.append(elem)

    def pop(self):
        return self.__stack.pop()

    def delete_elem(self, elem_to_delete):
        if not self.is_empty():
            elem = self.pop()
            if elem != elem_to_delete:
                self.delete_elem(elem_to_delete)
                self.add(elem)

    def is_empty(self):
        if len(self.__stack) == 0:
            return True
        return False

    def __str__(self):
        return '; '.join(self.__stack)
        # return str(self.__stack)