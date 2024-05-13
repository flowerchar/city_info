import random
import tkinter as tk
from tkinter import messagebox

class ArithmeticTestApp:
    def __init__(self, root):
        self.root = root
        self.root.title("小学生算术测试系统")

        self.current_question = 0
        self.score = 0
        self.questions = []

        self.name_label = tk.Label(root, text="请输入你的姓名：")
        self.name_label.pack()
        self.name_entry = tk.Entry(root)
        self.name_entry.pack()

        self.start_button = tk.Button(root, text="开始测试", command=self.start_test)
        self.start_button.pack()

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
        self.question_label.config(text=f"第{self.current_question + 1}题：")
        num1, operator, num2 = self.questions[self.current_question]
        self.question_text.set(f"{num1} {operator} {num2} = ")

    def start_test(self):
        student_name = self.name_entry.get()
        if not student_name:
            messagebox.showerror("错误", "请输入你的姓名！")
            return
        self.questions = [self.generate_question() for _ in range(10)]
        self.current_question = 0
        self.score = 0

        self.name_label.destroy()
        self.name_entry.destroy()
        self.start_button.destroy()

        self.question_label = tk.Label(self.root, text="")
        self.question_label.pack()
        self.question_text = tk.StringVar()
        self.question_entry = tk.Entry(self.root, textvariable=self.question_text)
        self.question_entry.pack()
        self.submit_button = tk.Button(self.root, text="提交答案", command=self.submit_answer)
        self.submit_button.pack()

        self.display_question()

    def submit_answer(self):
        try:
            user_answer = int(self.question_text.get().strip())
        except ValueError:
            messagebox.showerror("错误", "请输入一个整数！")
            return
        self.next_question(user_answer)

    def show_score(self):
        messagebox.showinfo("测试结束", f"你的得分是：{self.score} / 10")

if __name__ == "__main__":
    root = tk.Tk()
    app = ArithmeticTestApp(root)
    root.mainloop()
