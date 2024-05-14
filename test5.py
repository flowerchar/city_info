import random
# def find_previous_element(target: str, data: list) -> int:
#     previous_element = None
#
#     for i, sublist in enumerate(data):
#         if sublist[1] == target:
#             if i > 0:
#                 previous_element = data[i][0]
#             break
#
#     return previous_element
#
# # 示例用法
# data = [[10000, "asd1", 100], [10001, "asd2", 100], [10002, "asd3", 100], [10005, "asd4", 100], [10002, "asd3", 100]]
# target = "asd3"
# result = find_previous_element(target, data)
# print(result)

# data = [
#     [10000, "asd1", 100],
#     [10001, "asd2", 100],
#     [10002, "asd3", 100],
#     [10005, "asd4", 100],
#     [10002, "asd3", 100]
# ]
#
# filtered_data = [sublist for sublist in data if 10002 in sublist]
# print(filtered_data)

# def average_score(data):
#     # 创建一个字典来存储每个学生的总分数和出现的次数
#     student_scores = {}
#
#     # 遍历大列表，计算每个学生的总分数和出现的次数
#     for student in data:
#         student_id, name, score = student  # 学号、姓名和分数
#         if student_id not in student_scores:
#             student_scores[student_id] = [score, 1, name]
#         else:
#             student_scores[student_id][0] += score
#             student_scores[student_id][1] += 1
#
#     # 计算每个学生的平均分，并组成列表返回
#     averages = []
#     for student_id, (total_score, count, name) in student_scores.items():
#         average_score = round(total_score / count, 2)  # 保留两位小数
#         averages.append([student_id, name, average_score])
#
#     # 按照平均成绩从大到小排序，如果平均成绩相同，则按照 ID 从小到大排序
#     sorted_averages = sorted(averages, key=lambda x: (-x[2], x[0]))
#
#     return sorted_averages
#
#
# # 示例用法
# data = [
#     [10000, "asd1", 101.5],
#     [10001, "asd2", 101.5],
#     [10002, "asd3", 80],
#     [10000, "asd1", 90],
#     [10001, "asd2", 90]
# ]
#
# sorted_averages = average_score(data)
# print(sorted_averages)
# print(random.randint(1,1))

print("WeiLi".istitle())