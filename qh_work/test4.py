# import calendar
# # 获取当前年份
# from datetime import datetime
# def print_year_calendar(year):
#     # 设置以星期天为一周的开始
#     cal = calendar.Calendar(firstweekday=6)  # 6代表星期天
#
#     # 打印每个月的日历
#     for month in range(1, 13):
#         print(f"{calendar.month_name[month]} {year}")
#         print("Su Mo Tu We Th Fr Sa")
#
#         month_days = cal.monthdayscalendar(year, month)
#         for week in month_days:
#             print(" ".join(f"{day:2}" if day != 0 else "  " for day in week))
#         print()
#
#
# current_year = datetime.now().year
#
# # 打印当前年的日历
# print_year_calendar(current_year)
from datetime import datetime

def is_leap_year(year):
    """判断是否为闰年"""
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def get_days_in_month(year, month):
    """获取某年某月的天数"""
    if month in {1, 3, 5, 7, 8, 10, 12}:
        return 31
    elif month in {4, 6, 9, 11}:
        return 30
    elif month == 2:
        return 29 if is_leap_year(year) else 28
    else:
        raise ValueError("Invalid month")

def zellers_congruence(year, month, day):
    """Zeller's Congruence算法计算某年某月某日是星期几 (0=Saturday, 1=Sunday, ..., 6=Friday)"""
    if month < 3:
        month += 12
        year -= 1
    K = year % 100
    J = year // 100
    h = (day + (13 * (month + 1)) // 5 + K + K // 4 + J // 4 + 5 * J) % 7
    return h

def get_first_day_of_month(year, month):
    """获取某年某月的第一天是星期几 (0=Sunday, 1=Monday, ..., 6=Saturday)"""
    day_of_week = zellers_congruence(year, month, 1)
    # 调整到 0=Sunday, 1=Monday, ..., 6=Saturday
    return (day_of_week + 6) % 7

def print_month_calendar(year, month):
    """打印某年某月的日历"""
    days_in_month = get_days_in_month(year, month)
    first_day = get_first_day_of_month(year, month)

    # 打印月份和年份
    print(f"{datetime(year, month, 1):%B} {year}".center(20))
    print("Sun Mon Tue Wed Thu Fri Sat")

    # 生成每个月的日期
    days = ["    "] * first_day + [f"{day:3} " for day in range(1, days_in_month + 1)]

    # 确保每周占用一行
    for i in range(0, len(days), 7):
        print("".join(days[i:i + 7]).rstrip())

    print()

def print_year_calendar(year):
    """打印某年的日历"""
    for month in range(1, 13):
        print_month_calendar(year, month)

if __name__ == '__main__':
    # 获取当前年份
    current_year = datetime.now().year

    # 打印当前年的日历
    print_year_calendar(current_year)



