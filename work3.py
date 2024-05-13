import random
from PyQt5 import QtWidgets, QtCore, QtGui

class ArithmeticTestApp(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.current_question = 0
        self.score = 0
        self.questions = []

        self.setWindowTitle("小学生算术测试系统")

        self.name_label = QtWidgets.QLabel("请输入你的姓名：")
        self.name_entry = QtWidgets.QLineEdit()
        self.start_button = QtWidgets.QPushButton("开始测试")
        self.start_button.clicked.connect(self.start_test)

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.name_label)
        layout.addWidget(self.name_entry)
        layout.addWidget(self.start_button)
        self.setLayout(layout)

    def generate_question(self):
        num1 = random.randint(0, 99)
        num2 = random.randint(0, 99)
        operator = random.choice(['+', '-', '*', '/'])
        if operator == '/':
            num2 = random.randint(1, num1)
            num1 = num1 * num2
        return num1, operator, num2

    def check_answer(self, num1, operator, num2, user_answer):
        if operator == '+':
            correct_answer = num1 + num2
        elif operator == '-':
            correct_answer = num1 - num2
        elif operator == '*':
            correct_answer = num1 * num2
        elif operator == '/':
            correct_answer = num1 // num2
        return user_answer == correct_answer

    def next_question(self, user_answer):
        num1, operator, num2 = self.questions[self.current_question]
        if self.check_answer(num1, operator, num2, user_answer):
            self.score += 1
        self.current_question += 1
        if self.current_question < 10:
            self.display_question()
        else:
            self.show_score()

    def display_question(self):
        num1, operator, num2 = self.questions[self.current_question]
        self.question_label.setText(f"第{self.current_question + 1}题：")
        self.question_text.setText(f"{num1} {operator} {num2} = ")

    def start_test(self):
        student_name = self.name_entry.text().strip()
        if not student_name:
            QtWidgets.QMessageBox.critical(self, "错误", "请输入你的姓名！")
            return
        self.questions = [self.generate_question() for _ in range(10)]
        self.current_question = 0
        self.score = 0

        self.name_label.deleteLater()
        self.name_entry.deleteLater()
        self.start_button.deleteLater()

        self.question_label = QtWidgets.QLabel()
        self.question_text = QtWidgets.QLabel()
        self.question_entry = QtWidgets.QLineEdit()
        self.submit_button = QtWidgets.QPushButton("提交答案")
        self.submit_button.clicked.connect(self.submit_answer)

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.question_label)
        layout.addWidget(self.question_text)
        layout.addWidget(self.question_entry)
        layout.addWidget(self.submit_button)
        self.setLayout(layout)

        self.display_question()

    def submit_answer(self):
        try:
            user_answer = int(self.question_entry.text().strip())
        except ValueError:
            QtWidgets.QMessageBox.critical(self, "错误", "请输入一个整数！")
            return
        self.next_question(user_answer)

    def show_score(self):
        QtWidgets.QMessageBox.information(self, "测试结束", f"你的得分是：{self.score} / 10")

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = ArithmeticTestApp()
    window.show()
    app.exec_()
