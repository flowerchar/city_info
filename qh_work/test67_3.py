import itertools
import random


def generate_numbers():
    """ 随机生成4个1~10之间的整数 """
    return [random.randint(1, 10) for _ in range(4)]

#
# def valid_result(nums, target=24):
#     """ 判断4个数字能否通过四则运算和括号变化得到目标值 """
#     if len(nums) == 1:
#         return abs(nums[0] - target) < 1e-6
#
#     # 遍历所有可能的数字排列和运算符组合
#     for i in range(len(nums)):
#         for j in range(len(nums)):
#             if i != j:
#                 # 剩余的数字
#                 nums_remaining = [nums[k] for k in range(len(nums)) if k != i and k != j]
#
#                 # 遍历所有可能的运算
#                 for op in "+-*/":
#                     if op in "+-*/" and (op != '/' or nums[j] != 0):  # 防止除以零
#                         if op == '+':
#                             new_num = nums[i] + nums[j]
#                         elif op == '-':
#                             new_num = nums[i] - nums[j]
#                         elif op == '*':
#                             new_num = nums[i] * nums[j]
#                         elif op == '/':
#                             new_num = nums[i] / nums[j]
#
#                         # 递归调用判断剩余数字能否得到目标值
#                         if valid_result(nums_remaining + [new_num], target):
#                             return True
#     return False


# 主程序
numbers = generate_numbers()
print(f"生成的数字是: {numbers}")
# if valid_result(numbers):
#     print("可以通过运算得到24。")
# else:
#     print("不能通过运算得到24。")

def dfs(nums):
    """ 使用深度优先搜索判断是否能通过四则运算得到24，并打印运算过程 """
    if len(nums) == 1:
        if abs(nums[0] - 24) < 1e-6:
            return (True, str(nums[0]))
        else:
            return (False, "")

    for i in range(len(nums)):
        for j in range(len(nums)):
            if i != j:
                # 剩余的数字
                nums_remaining = [nums[k] for k in range(len(nums)) if k != i and k != j]

                # 遍历所有可能的运算
                for op in "+-*/":
                    if (op == '+' or op == '*') and i > j:
                        continue  # 避免重复计算对称情况（交换律）

                    if op == '+':
                        new_num = nums[i] + nums[j]
                        expr = f"({nums[i]} + {nums[j]})"
                    elif op == '-':
                        new_num = nums[i] - nums[j]
                        expr = f"({nums[i]} - {nums[j]})"
                    elif op == '*':
                        new_num = nums[i] * nums[j]
                        expr = f"({nums[i]} * {nums[j]})"
                    elif op == '/' and nums[j] != 0:
                        new_num = nums[i] / nums[j]
                        expr = f"({nums[i]} / {nums[j]})"
                    else:
                        continue

                    success, sub_expr = dfs(nums_remaining + [new_num])
                    if success:
                        return (True, sub_expr.replace(str(new_num), expr, 1))
    return (False, "")


def can_reach_24(numbers):
    """ 主函数：判断4个数字能否通过四则运算得到24，并返回计算过程 """
    success, expr = dfs(numbers)
    return success, expr


# 示例

success, expression = can_reach_24(numbers)
if success:
    print(f"可以通过运算得到24: {expression} = 24")
else:
    print("不能通过运算得到24。")
