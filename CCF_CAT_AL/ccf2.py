def make_string(s):
    """
    将字符串整理好，满足相邻字符不为大小写相同的字母。

    :param s: 由大小写英文字母组成的字符串
    :return: 整理好的字符串
    """
    stack = []
    for char in s:
        if stack and ((stack[-1].lower() == char.lower()) and (stack[-1] != char)):
            stack.pop()
        else:
            stack.append(char)
    return ''.join(stack)


def main():
    # 读取输入，格式：str = "HogGgwarts"
    input_str = input("输入: ")
    # 调用函数并输出结果
    result = make_string(input_str)
    print(f"输出: {result}")


# 示例测试
if __name__ == "__main__":
    main()
