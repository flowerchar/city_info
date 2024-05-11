#!/usr/bin/env python
# coding: utf-8

# ##  定期利息

# In[3]:


a,b=eval(input())
c=a*(100+b)/100
print(c)


# ## 活期利息

# In[4]:


a,b=eval(input())
c=a*(100+b)/100
print(c)
c=c*(100+b)/100
print(c)


# ## 阶乘之和

# In[5]:


import math
a,b=eval(input())
c=math.factorial(a)+math.factorial(b)
print(c)

# In[6]
# 习题一：计算一年期满后本金与利息总额
def calculate_total(principal:float, interest_rate:float)->float:
    interest = principal * (interest_rate / 100)
    total = principal + interest
    return total

# 习题二：计算自动转存一次和两次后的期满金额
def auto_renew(principal:float, interest_rate:float, times:int=1)->float:
    total = principal
    for _ in range(times):
        total = calculate_total(total, interest_rate)
    return total

# 习题三：求两个整数的阶乘之和
def factorial_sum(num1:int, num2:int)->int:
    def factorial(n):
        return 1 if n == 0 else n*factorial(n-1)
    return factorial(num1) + factorial(num2)

try:
    # 示例用法
    # 习题一
    principal = float(input("请输入存款本金（人民币元）："))
    interest_rate = float(input("请输入存款利率（年利率，不需要输入百分号）："))
    total_amount = calculate_total(principal, interest_rate)
    print("一年期满后的本金与利息总额为：", total_amount)

    # 习题二
    principal = float(input("请输入存款本金（人民币元）："))
    interest_rate = float(input("请输入存款利率（年利率，不需要输入百分号）："))
    # times = int(input("请输入自动转存的次数："))
    total_amount1 = auto_renew(principal, interest_rate)
    total_amount2 = auto_renew(principal, interest_rate, 2)
    print(f"自动转存 {1} 次后的期满金额为：{total_amount1}")
    print(f"自动转存 {2} 次后的期满金额为：{total_amount2}")

    # 习题三
    num1 = int(input("请输入第一个整数："))
    num2 = int(input("请输入第二个整数："))
    sum_of_factorials = factorial_sum(num1, num2)
    print("两个整数的阶乘之和为：", sum_of_factorials)
except Exception as e:
    print("输入的数据格式有误！", e)
