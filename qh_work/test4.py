import calendar
# 获取当前年份
from datetime import datetime
def print_year_calendar(year):
    # 设置以星期天为一周的开始
    cal = calendar.Calendar(firstweekday=6)  # 6代表星期天

    # 打印每个月的日历
    for month in range(1, 13):
        print(f"{calendar.month_name[month]} {year}")
        print("Su Mo Tu We Th Fr Sa")

        month_days = cal.monthdayscalendar(year, month)
        for week in month_days:
            print(" ".join(f"{day:2}" if day != 0 else "  " for day in week))
        print()


current_year = datetime.now().year

# 打印当前年的日历
print_year_calendar(current_year)
