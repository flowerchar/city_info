
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


def generate_month_calendar(year, month):
    """生成某年某月的日历文本"""
    days_in_month = get_days_in_month(year, month)
    first_day = get_first_day_of_month(year, month)

    header = f"{datetime(year, month, 1):%B} {year}".center(20)
    week_header = "Su Mo Tu We Th Fr Sa"
    weeks = [[]]

    # 填充第一周之前的空格
    for _ in range(first_day):
        weeks[0].append("  ")

    # 填充每一天的日期
    for day in range(1, days_in_month + 1):
        weeks[-1].append(f"{day:2}")
        if len(weeks[-1]) == 7:
            weeks.append([])

    # 确保所有周都有7天
    while len(weeks[-1]) < 7:
        weeks[-1].append("  ")

    # 将日历的每周格式化为字符串
    weeks = [" ".join(week) for week in weeks]
    return [header, week_header] + weeks


def print_quarter_calendar(year, start_month):
    """打印某一季度的日历"""
    months = [generate_month_calendar(year, month) for month in range(start_month, start_month + 3)]
    max_lines = max(len(month) for month in months)

    # 统一长度
    for month in months:
        while len(month) < max_lines:
            month.append(" " * 20)

    # 打印季度的三个月份日历
    for lines in zip(*months):
        print("     ".join(lines))  # 调整列之间的空格


def print_full_year_calendar(year):
    """打印某年的日历"""
    for start_month in range(1, 13, 3):  # 每次增加 3，以打印季度
        print_quarter_calendar(year, start_month)
        print()  # 每个季度之间空行


# 获取当前年份
current_year = datetime.now().year

# 打印当前年的日历
print_full_year_calendar(current_year)

