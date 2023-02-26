class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):  # 判断栈是否为空
        return self.items == []

    def size(self):  # 获取栈中元素的个数
        return len(self.items)

    def push(self, item):  # 入栈
        self.items.append(item)

    def pop(self):  # 出栈
        return self.items.pop()

    def top(self):  # 获取栈顶元素
        if len(self.items):
            return self.items[len(self.items) - 1]
        return None
    def display(self):
        for i in self.items:
            print(i,end = ' ')
        print('\t',end = '')