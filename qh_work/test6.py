import calendar
# 获取当前年份
from datetime import datetime
def print_full_year_calendar(year):
    # 创建一个文本日历实例
    cal = calendar.TextCalendar(firstweekday=6)  # 6代表星期天

    # 存储所有月份的日历
    months = [cal.formatmonth(year, month) for month in range(1, 13)]

    # 分割为每行三个月
    lines_per_month = len(months[0].split('\n'))
    month_chunks = [months[i:i+3] for i in range(0, len(months), 3)]

    # 打印每行的月份
    for chunk in month_chunks:
        month_lines = [month.split('\n') for month in chunk]
        for i in range(lines_per_month):
            for month in month_lines:
                print(month[i].ljust(22), end=' ')  # 每个月份宽度设置为22个字符
            print()  # 换行


current_year = datetime.now().year

# 打印当前年的日历
print_full_year_calendar(current_year)
