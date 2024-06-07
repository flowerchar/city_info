def pass_the_flower(n, s):
    """
    计算s秒后拿着花的人的编号

    :param n: 人数
    :param s: 秒数
    :return: s秒后拿着花的人的编号
    """
    # 初始位置在队首
    position = 1
    # 初始方向为向右（1表示向右，-1表示向左）
    direction = 1

    # 每秒钟更新花的位置
    for _ in range(s):
        # 更新位置
        position += direction

        # 如果到达队首或队尾，改变方向
        if position == 1:
            direction = 1  # 向右传递
        elif position == n:
            direction = -1  # 向左传递

    return position


# 主程序
def main():
    # 读取输入
    # 按照文档给的格式输入：n = 4, s = 5
    # 输入的时候不要有空格：n=4, s=5
    input_str = input("输入：")
    # 解析输入
    parts = input_str.split(", ")
    n = int(parts[0].split(" = ")[1])
    s = int(parts[1].split(" = ")[1])

    # 调用函数并输出结果
    result = pass_the_flower(n, s)
    print(result)


# 示例测试
if __name__ == "__main__":
    main()
