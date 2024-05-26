import calendar
# 示例使用
from datetime import datetime
from time import time

def write_year_calendar_to_file(year, file_path):
    # 设置以星期天为一周的开始
    cal = calendar.Calendar(firstweekday=6)  # 6代表星期天

    with open(file_path, 'w', encoding='utf-8') as file:
        # 遍历每个月，生成每个月的日历
        for month in range(1, 13):
            file.write(f"{calendar.month_name[month]} {year}\n")
            file.write("Su Mo Tu We Th Fr Sa\n")

            month_days = cal.monthdayscalendar(year, month)
            for week in month_days:
                file.write(" ".join(f"{day:2}" if day != 0 else "  " for day in week) + '\n')
            file.write('\n')  # 添加空行分隔各月

    print(f"The calendar for the year {year} has been written to {file_path}")




current_year = datetime.now().year

# 调用函数生成并输出日历到文件，加上时间戳以避免重名
file_path = f'year_calendar{str(time())[-3::]}.txt'
write_year_calendar_to_file(current_year, file_path)
