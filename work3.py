import random
import os

class AdminSystem:
    def __init__(self):
        self.students = []
        self.records_file = "record.txt"
        self.current_student_name = None


    def init(self) -> None:
        '''
        初始化函数，用于读取record.txt文件中的数据；也可以是测评后更新数据
        :return:
        '''
        # 如果不存在record.txt文件，创建一个空文件
        if self.students is not None:
            # 说明是非第一次调用init函数
            self.students.clear()
        if not os.path.exists(self.records_file):
            with open(self.records_file, 'w'):
                return
        with open(self.records_file, 'r') as file:
            for line in file:
                student = line.strip().split(',')
                student = [int(student[0]), student[1], int(student[2])]
                self.students.append(student)

    def generate_id(self) -> int:
        '''
        生成学生ID
        :return: 返回从100001到999999之间的一个递增的数字
        '''
        if not self.students:
            student_id = 100001
        else:
            id_list = [int(student[0]) for student in self.students]
            student_id = max(id_list) + 1
            if student_id > 999999:
                raise ValueError("学生ID已达到上限！")
        return student_id


    def generate_question(self) -> tuple:
        '''
        生成算术题
        :return: 数字1，运算符，数字2
        '''
        # 生成算术题
        num1 = random.randint(0, 99)
        num2 = random.randint(0, 99)
        operator = random.choice(['+', '-', '*', '/'])
        if operator == '/':
            if num1 == 0:
                num1 = random.randint(1, 99)
                # 为了避免randint出错，重新生成num1
            num2 = random.randint(1, num1)  # 保证可以整除，且除数不为0
            num1 = num1 * num2  # 修改num1，使得结果正确
        answer = eval(f"{num1} {operator} {num2}")
        if not(0 < answer < 100) or (num1 > 100 or num2 > 100):
            return self.generate_question()
        return num1, operator, num2


    def check_answer(self, num1: int, operator: str, num2: int, user_answer: float) -> bool:
        '''
        检查答案是否正确
        :param num1:
        :param operator:
        :param num2:
        :param user_answer:
        :return:
        '''
        # 检查答案是否正确
        if operator == '+':
            correct_answer = num1 + num2
        elif operator == '-':
            correct_answer = num1 - num2
        elif operator == '*':
            correct_answer = num1 * num2
        elif operator == '/':
            correct_answer = num1 // num2
        return user_answer == correct_answer


    def record_score(self, file_name:str, student_id:int, current_student_name:str, score:float) -> None:
        '''
        记录学生成绩
        :param file_name:
        :param student_id:
        :param current_student_name:
        :param score:
        :return:
        '''
        # 记录学生成绩
        with open(file_name, 'a') as file:
            file.write(f"{student_id},{current_student_name},{score}\n")


    def find_id_by_name(self, name: str, data: list) -> int:
        '''
        通过姓名查找学生ID
        :param name:
        :param data:
        :return: 学生ID
        '''
        student_id = None

        for i, sublist in enumerate(data):
            if sublist[1] == name:
                # if i > 0:
                student_id = data[i][0]
            break

        return student_id

    def check_name_pattern(self, name: str) -> bool:
        '''
        检查姓名格式是否正确
        :param name:
        :return:
        '''
        try:
            name_list = name.split(' ')
            if len(name_list) != 2:
                return False
            else:
                for i in name_list:
                    if not (i.isalpha() and i[0].isupper()):
                        # 这层判断包括为字母并且首字母大写
                        return False
                return True
        except ValueError:
            return False

    def average_score(self, data:list) -> list:
        '''
        计算学生的平均分
        :param data:
        :return: 按照指定顺序排序的学生平均分列表
        '''
        # 创建一个字典来存储每个学生的总分数和出现的次数
        student_scores = {}

        # 遍历大列表，计算每个学生的总分数和出现的次数
        for student in data:
            student_id, name, score = student  # 学号、姓名和分数
            if student_id not in student_scores:
                student_scores[student_id] = [score, 1, name]
            else:
                student_scores[student_id][0] += score
                student_scores[student_id][1] += 1

        # 计算每个学生的平均分，并组成列表返回
        averages = []
        for student_id, (total_score, count, name) in student_scores.items():
            average_score = round(total_score / count, 2)  # 保留两位小数
            averages.append([student_id, name, average_score])

        # 按照平均成绩从大到小排序，如果平均成绩相同，则按照 ID 从小到大排序
        sorted_averages = sorted(averages, key=lambda x: (-x[2], x[0]))

        return sorted_averages



    def main(self):
        '''
        主函数
        :return:
        '''
        # 主函数
        self.current_student_name = input("请输入你的姓名：" ).strip()
        if not self.check_name_pattern(self.current_student_name):
            print("姓名输入有误，请重新输入！")
            return
        self.init()

        while True:
            print("\n1. 开始测试")
            print("2. 成绩查询")
            print("3. 成绩排序")
            print("4. 退出")
            choice = input("请选择操作：")

            if choice == '1':
                # current_student_name = input("请输入你的姓名：")
                name_list = [student[1] for student in self.students]
                if self.current_student_name not in name_list:
                    student_id = self.generate_id()
                    # students.append([student_id, current_student_name, 0])
                else:
                    student_id = self.find_id_by_name(self.current_student_name, self.students)
                    # students.append([student_id, current_student_name, 0])
                print("你的ID是：", student_id)
                score = 0
                i = 1
                while i <= 10:
                    num1, operator, num2 = self.generate_question()
                    try:
                        user_answer = float(input(f"第{i}题：{num1} {operator} {num2} = "))
                    except ValueError:
                        print("输入有误，请重新输入！")
                        continue
                    if self.check_answer(num1, operator, num2, user_answer):
                        print("回答正确！")
                        score += 1
                    else:
                        print("回答错误！")
                    i += 1
                self.record_score(self.records_file, student_id, self.current_student_name, score)
                self.init()
                print("你的得分是：", score)

            elif choice == '2':
                search_key = input("请输入要查询的学生姓名或ID：")
                if "100001" <= search_key <= "999999" and search_key.isdigit():
                    # 是id
                    search_key = int(search_key)
                # else:
                #     pass
                filtered_data = [sublist for sublist in self.students if search_key in sublist]
                # records = read_records(records_file)
                # search_result = search_student(records, search_key)
                if filtered_data:
                    # found_records, average_score = search_result
                    print(f"学生{search_key}的历史得分为：")
                    for index, record in enumerate(filtered_data, start=1):
                        print(f"第{index}次测评得分: {record[2]}")  # 学号: {record[0]}, 姓名: {record[1]},
                    total_score = sum([sublist[-1] for sublist in filtered_data])
                    times = len(filtered_data)
                    print(f"总和成绩为：{total_score}，经过{times}次测评，平均得分为：{total_score/times:.2f}")
                else:
                    print("未找到该学生的记录！")

            elif choice == '3':
                average_score_list = self.average_score(self.students)
                print("按平均分排序的学生名单：")
                for i, record in enumerate(average_score_list, start=1):
                    print(f"第{i}名: 学号: {record[0]}, 姓名: {record[1]}, 平均得分: {record[2]}")

            elif choice == '4':
                break

            else:
                print("无效选项，请重新输入！")

class Student:
    def __init__(self, name: str, student_id: int):
        self.name = name
        self.student_id = student_id
        self.records = []

    def average_score(self) -> float:
        return sum(self.records) / len(self.records)
    def __str__(self):
        return f"学号：{self.student_id}， 姓名：{self.name}， 平均得分：{self.average_score():.2f}"

if __name__ == "__main__":
    admin = AdminSystem()
    admin.main()
