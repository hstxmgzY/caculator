class Stack:
    def __init__(self):
        self.__list = []

    def is_empty(self):
        return self.__list == []

    def push(self, item):
        self.__list.append(item)

    def pop(self):
        if self.is_empty():
            return
        else:
            return self.__list.pop()

    def top(self):
        if self.is_empty():
            return
        else:
            return self.__list[-1]