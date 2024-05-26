import re


def is_line_palindrome(line):
    # 提取所有字母和空格，并转换为小写
    letters_and_spaces = re.findall(r'[a-zA-Z ]', line)
    original_sequence = ''.join(letters_and_spaces).lower()

    # 判断字母和空格序列是否为回文
    return original_sequence == original_sequence[::-1]


def check_palindrome_lines(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
    except FileNotFoundError:
        print(f"File {file_path} not found.")
        return

    for line in lines:
        line = line.strip()
        if is_line_palindrome(line):
            print(f"'{line}' is a palindrome line.")
        else:
            print(f"'{line}' is not a palindrome line.")

# 检查并输出每一行是否为回文
file_path = 'example.txt'
check_palindrome_lines(file_path)
