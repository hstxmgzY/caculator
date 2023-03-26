import sys

from PyQt6.QtCore import pyqtSignal
from PyQt6.QtGui import QTextCursor
from PyQt6.QtWidgets import QWidget, QApplication, QMessageBox
from caculator import Stack
from stack import Ui_Dialog


def judge_leg(string):
    # 表达式的合法性
    # 括号配对
    mystack = Stack()
    for c in string:
        if c == '(':
            mystack.push('(')
        if c == ')':
            if mystack.is_empty():
                return 0
            else:
                mystack.pop()
    if not mystack.is_empty():
        return 0

    # 将表达式分离数字以及符号,并判断表达式的合理性
    list_all = []
    list_op = ['+', '-', '*', '/', '(', ')', '~']
    for i in string:
        list_all.append(i)

    # i = 0
    # while i <= len(list_all) - 1:
    #     if list_all[i] not in list_op and i != len(list_all) - 1 and list_all[i + 1] not in list_op:
    #         list_all[i] = list_all[i] + list_all[i + 1]
    #         del list_all[i + 1]
    #         i = i - 1
    #     i = i + 1
    #
    # op = 0
    # num = 0
    #
    # for i in range(len(list_all)):
    #     if list_all[i] == '(' and i != 0:  # 左括号的右边是操作符，左边是数字
    #         if list_all[i - 1] not in list_op or list_all[i + 1] in list_op:
    #             return 0
    #     if list_all[i] == ')' and i != len(list_all) - 1:  # 右括号的右边是数字，左边是操作符
    #         if list_all[i - 1] in list_op or list_all[i + 1] not in list_op:
    #             return 0
    #     if list_all[i] in list_op and list_all[i + 1] in list_op and i != len(list_all) - 1:
    #         return 0
    #     if list_all[i] != ')' and list_all[i] != '(' and list_all[i] in list_op:
    #         op = op + 1
    #     if list_all[i] not in list_op:
    #         num = num + 1
    # if num != op + 1:
    #     return 0

    return list_all


def caltrans(a, b, op):
    a = float(a)
    b = float(b)
    if op == '+':
        res = a + b
        if res.is_integer():
            res = int(res)
        return res
    if op == '-':
        res = a - b
        if res.is_integer():
            res = int(res)
        return res
    if op == '*':
        res = a * b
        if res.is_integer():
            res = int(res)
        return res
    if op == '/':
        res = a / b
        if res.is_integer():
            res = int(res)
        return res


def to_postfix(list_all):
    list_op = ['+', '-', '*', '/', '(', ')']
    dict_order = {'+': 1, '-': 1, '*': 2, '/': 2, '(': 0}
    list_res = []
    mystack = Stack()
    for i in list_all:
        if i not in list_op:
            list_res.append(i)
        else:
            if i == '(':
                mystack.push(i)
            elif i == ')':
                while mystack.top() != '(':
                    list_res.append(mystack.top())
                    mystack.pop()
                mystack.pop()
            elif i == '~':
                # 处理负号
                j = list_all.index(i)
                if j == 0 or list_all[j - 1] in list_op:
                    # 表示负数
                    neg_num = '-' + list_all[j + 1]
                    list_res.append(neg_num)
                else:
                    mystack.push(i)
            else:
                if mystack.is_empty():
                    mystack.push(i)
                else:
                    if dict_order[i] > dict_order[mystack.top()]:
                        mystack.push(i)
                    else:
                        while not mystack.is_empty() and dict_order[i] <= dict_order[mystack.top()]:
                            list_res.append(mystack.top())
                            mystack.pop()
                        mystack.push(i)

    while not mystack.is_empty():
        list_res.append(mystack.top())
        mystack.pop()
    return list_res


def cal(list_res):  # 计算后缀表达式
    list_op = ['+', '-', '*', '/', ')', '(']
    mystack = Stack()
    for c in list_res:
        if c not in list_op:
            mystack.push(c)
        else:
            a = mystack.top()
            mystack.pop()
            b = mystack.top()
            mystack.pop()
            mystack.push(caltrans(b, a, c))

    return mystack.top()


class MyWindow(QWidget, Ui_Dialog):
    signal = pyqtSignal(str)

    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        self.setupUi(self)
        self.setup_connections()
        cursor = self.display.textCursor()
        cursor.movePosition(QTextCursor.MoveOperation.End)
        self.display.setTextCursor(cursor)

    def setup_connections(self):
        # 数字按钮
        self.btn0.clicked.connect(lambda: self.add_to_display('0'))
        self.btn1.clicked.connect(lambda: self.add_to_display('1'))
        self.btn2.clicked.connect(lambda: self.add_to_display('2'))
        self.btn3.clicked.connect(lambda: self.add_to_display('3'))
        self.btn4.clicked.connect(lambda: self.add_to_display('4'))
        self.btn5.clicked.connect(lambda: self.add_to_display('5'))
        self.btn6.clicked.connect(lambda: self.add_to_display('6'))
        self.btn7.clicked.connect(lambda: self.add_to_display('7'))
        self.btn8.clicked.connect(lambda: self.add_to_display('8'))
        self.btn9.clicked.connect(lambda: self.add_to_display('9'))
        self.dot.clicked.connect(lambda: self.add_to_display('.'))
        # 操作按钮
        self.add.clicked.connect(lambda: self.add_to_display('+'))
        self.sub.clicked.connect(lambda: self.add_to_display('-'))
        self.mul.clicked.connect(lambda: self.add_to_display('*'))
        self.div.clicked.connect(lambda: self.add_to_display('/'))
        self.leftbrack.clicked.connect(lambda: self.add_to_display('('))
        self.rightbrack.clicked.connect(lambda: self.add_to_display(')'))
        # 其他按钮
        self.dele.clicked.connect(lambda: self.delete_display())
        self.ac.clicked.connect(lambda: self.clear_display())
        self.equal.clicked.connect(lambda: self.calculate())
        self.exit.clicked.connect(self.click_button)

    def add_to_display(self, value):
        if self.display.toPlainText() == '0' and '0' <= value <= '9':
            self.display.clear()
        #if self.display.toPlainText()[0] in ['+', '-', '*', '/']:
         #   self.content(self.click_error())
        self.display.insertPlainText(value)

    def delete_display(self):
        cursor = self.display.textCursor()
        cursor.deletePreviousChar()

    def clear_display(self):
        self.display.setText('0')
        cursor = self.display.textCursor()
        cursor.movePosition(QTextCursor.MoveOperation.End)
        self.display.setTextCursor(cursor)

    def calculate(self):
        string = self.display.toPlainText()
        if judge_leg(string) == 0:
            self.display.setText('Error！')
        else:
            self.display.setText(str(cal(to_postfix(judge_leg(string)))))
        cursor = self.display.textCursor()
        cursor.movePosition(QTextCursor.MoveOperation.End)
        self.display.setTextCursor(cursor)

    def click_button(self):
        confirm_exit = QMessageBox.question(
            self, "提示", "你确定要退出吗😭",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No, QMessageBox.StandardButton.No)
        if confirm_exit == QMessageBox.StandardButton.Yes:
            QApplication.quit()

    def click_error(self):
        QMessageBox.question(self, "提示", "第一位数不可以是符号，请重新输入")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec())
