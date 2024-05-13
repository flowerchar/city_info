import random
def digit_sum(n):
    # 计算各位数字之和
    total_sum = sum(int(digit) for digit in str(n))
    return total_sum

def find_desired_number(n):
    # 重复计算各位数字之和，直到结果在1~9之间
    while n not in range(1, 10):
        n = digit_sum(n)
    return n

# 测试
number = 123456
result = find_desired_number(number)
# print("The result is:", result)

def calculate_ratio():
    total_numbers = 99999
    digit_counts = {digit: 0 for digit in range(1, 10)}

    for i in range(1, total_numbers):
        result = find_desired_number(i)
        digit_counts[result] += 1

    # 计算1~9出现的比例
    ratio = {digit: digit_counts[digit] / total_numbers for digit in range(1, 10)}
    return ratio

# 测试
result_ratio = calculate_ratio()
# print("Ratio of occurrence for digits 1-9:", result_ratio)

def factorial(n):
    # 计算阶乘
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def combination(n, k):
    # 计算组合数C(n, k)
    if k == 0 or k == n:
        return 1
    else:
        return factorial(n) // (factorial(k) * factorial(n - k))

# 测试
n = 10
k = 3
result = combination(n, k)
# print(f"C({n},{k}) = {result}")



def estimate_pi(num_points):
    points_inside_circle = 0

    for _ in range(num_points):
        # 在四分之一正方形内随机生成点
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)

        # 判断点是否在四分之一圆内（半径为1）
        if x**2 + y**2 <= 1:
            points_inside_circle += 1

    # 计算落在四分之一圆内的点的比例
    ratio = points_inside_circle / num_points

    # 圆周率的近似值为四分之一圆内点的比例乘以4
    pi_estimate = ratio * 4
    return pi_estimate

# 测试
num_points = 1000000  # 改变这个值来增加或减少随机生成的点的数量
estimated_pi = estimate_pi(num_points)
print("Estimated value of pi:", estimated_pi)
