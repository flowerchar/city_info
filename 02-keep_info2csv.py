
import csv

# 数据
data = [
    ["Name", "Age", "City"],
    ["Alice", "23", "New York"],
    ["Bob", "28", "Los Angeles"],
    ["Charlie", "22", "Chicago"]
]

# 打开一个文件用于写入。如果文件不存在，它将被创建。
with open('example.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)

print("CSV文件已创建并写入数据。")