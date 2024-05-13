import random
import os
from typing import List
students = []
# [[10000, "asd", 100], [10001, "asd", 100], [10002, "asd", 100]]  : List[List[int, str, float]]
def init():
    # 如果不存在record.txt文件，创建一个空文件
    global students
    if not os.path.exists("record.txt"):
        with open("record.txt", 'w'):
            return
    with open("record.txt", 'r') as file:
        for line in file:
            student = line.strip().split(',')
            student = [int(student[0]), student[1], int(student[2])]
            students.append(student)

def generate_id():
    # 我希望这个函数返回从100001到999999之间的一个递增的数字，我不希望是随机的，而是递增不重复的，实现代码
    if not students:
        student_id = 100001
    else:
        id_list = [int(student[0]) for student in students]
        student_id = max(id_list) + 1
        if student_id > 999999:
            raise ValueError("学生ID已达到上限！")
    return student_id


def generate_question() -> tuple:
    # 生成算术题
    num1 = random.randint(0, 99)
    num2 = random.randint(0, 99)
    operator = random.choice(['+', '-', '*', '/'])
    if operator == '/':
        num2 = random.randint(1, num1)  # 保证可以整除，且除数不为0
        num1 = num1 * num2  # 修改num1，使得结果正确
    answer = eval(f"{num1} {operator} {num2}")
    if not(0 < answer < 100) or (num1 > 100 or num2 > 100):
        return generate_question()
    return num1, operator, num2


def check_answer(num1: int, operator: str, num2: int, user_answer: float) -> bool:
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


def record_score(file_name, student_id, current_student_name, score):
    # 记录学生成绩
    with open(file_name, 'a') as file:
        file.write(f"{student_id},{current_student_name},{score}\n")


def read_records(file_name):
    # 读取记录文件
    records = []
    with open(file_name, 'r') as file:
        for line in file:
            record = line.strip().split(',')
            records.append(record)
    return records


def calculate_average_score(records):
    # 计算平均分
    total_score = sum(int(record[2]) for record in records)
    return round(total_score / len(records), 2)


def search_student(records, search_key):
    # 查询学生记录
    found_records = [record for record in records if search_key in record[:2]]
    if not found_records:
        return None
    average_score = calculate_average_score(found_records)
    return found_records, average_score


def sort_students(records):
    # 按平均分排序学生
    sorted_records = sorted(records, key=lambda x: (-calculate_average_score(x), int(x[0])))
    return sorted_records

def find_id_by_name(name: str, data: list) -> int:
    student_id = None

    for i, sublist in enumerate(data):
        if sublist[1] == name:
            if i > 0:
                student_id = data[i][0]
            break

    return student_id

def average_score(data):
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



def main():
    # 主函数

    records_file = "record.txt"
    current_student_name = input("请输入你的姓名：" )
    init()

    while True:
        print("\n1. 开始测试")
        print("2. 成绩查询")
        print("3. 成绩排序")
        print("4. 退出")
        choice = input("请选择操作：")

        if choice == '1':
            # current_student_name = input("请输入你的姓名：")
            name_list = [student[1] for student in students]
            if current_student_name not in name_list:
                student_id = generate_id()
                # students.append([student_id, current_student_name, 0])
            else:
                student_id = find_id_by_name(current_student_name, students)
                # students.append([student_id, current_student_name, 0])
            print("你的ID是：", student_id)
            score = 0
            i = 1
            while i <= 10:
                num1, operator, num2 = generate_question()
                try:
                    user_answer = int(input(f"第{i}题：{num1} {operator} {num2} = "))
                except ValueError:
                    print("输入有误，请重新输入！")
                    continue
                if check_answer(num1, operator, num2, user_answer):
                    print("回答正确！")
                    score += 1
                else:
                    print("回答错误！")
                i += 1
            record_score(records_file, student_id, current_student_name, score)
            print("你的得分是：", score)

        elif choice == '2':
            search_key = input("请输入要查询的学生姓名或ID：")
            # if "100001" <= search_key <= "999999":
            #     pass
            # else:
            #     pass
            filtered_data = [sublist for sublist in students if search_key in sublist]
            # records = read_records(records_file)
            # search_result = search_student(records, search_key)
            if filtered_data:
                # found_records, average_score = search_result
                print(f"学生{search_key}的历史得分为：")
                for record in filtered_data:
                    print(f"ID: {record[0]}, 姓名: {record[1]}, 得分: {record[2]}")
                print(f"平均得分为：{sum([sublist[-1] for sublist in filtered_data])/len(filtered_data):.2f}")
            else:
                print("未找到该学生的记录！")

        elif choice == '3':
            average_score_list = average_score(students)
            print("按平均分排序的学生名单：")
            for i, record in enumerate(average_score_list, start=1):
                print(f"第{i}名: ID: {record[0]}, 姓名: {record[1]}, 平均得分: {record[2]}")

        elif choice == '4':
            break

        else:
            print("无效选项，请重新输入！")


if __name__ == "__main__":
    main()
