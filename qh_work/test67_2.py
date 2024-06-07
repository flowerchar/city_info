def precedence(op):
    """ 返回操作符的优先级 """
    if op in ('+', '-'):
        return 1
    if op in ('*', '/'):
        return 2
    return 0

def apply_op(a, b, op):
    """ 应用操作符 op 计算 a 和 b 的结果 """
    if op == '+': return a + b
    if op == '-': return a - b
    if op == '*': return a * b
    if op == '/': return a / b

def infix_to_postfix(expression):
    """ 将中缀表达式转换为后缀表达式 """
    stack = []  # 用于存储操作符
    output = []  # 用于存储后缀表达式
    i = 0
    while i < len(expression):
        if expression[i].isdigit():
            # 如果是数字，读取完整的数字（处理多位数）
            num = []
            while i < len(expression) and expression[i].isdigit():
                num.append(expression[i])
                i += 1
            output.append(''.join(num))
            continue  # 已经处理过 i 的自增
        elif expression[i] in "+-*/":
            while stack and precedence(stack[-1]) >= precedence(expression[i]):
                output.append(stack.pop())
            stack.append(expression[i])
        i += 1
    while stack:
        output.append(stack.pop())
    return output

def evaluate_postfix(expression):
    """ 计算后缀表达式的值 """
    stack = []
    for token in expression:
        if token.isdigit():
            stack.append(int(token))
        else:
            b = stack.pop()
            a = stack.pop()
            stack.append(apply_op(a, b, token))
    return stack[0]

def evaluate_expression(expression):
    """ 主函数：接受用户输入的四则运算表达式，并计算结果 """
    postfix = infix_to_postfix(expression)
    return evaluate_postfix(postfix)

# 示例使用
input_expr = input("请输入一个四则运算表达式（如 '1-2+3*4'）：")
result = evaluate_expression(input_expr)
print(f"表达式的计算结果是: {result}")
