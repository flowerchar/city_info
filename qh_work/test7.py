# 判断是否为闰年
def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        return True
    else:
        return False


# 计算本年之前的天数
def sum_year_day(year):
    begain = 1921  # 我们这里选择1921年为起始年
    sum1 = 0
    while begain < year:
        if is_leap_year(begain):
            sum1 = sum1 + 366
        else:
            sum1 = sum1 + 365
        begain = begain + 1
    return sum1


# 计算本年中本月之前的天数
def sum_month_day(year, month):
    i = 1
    sum2 = 0
    while i < month:  # 判断月份获取天数
        if i == 1 or i == 3 or i == 5 or i == 7 or i == 8 or i == 10 or i == 12:
            sum2 = sum2 + 31
        elif i == 2:  # 2月份时，判断是否为闰年
            if is_leap_year(year):
                sum2 = sum2 + 29
            else:
                sum2 = sum2 + 28
        else:
            sum2 = sum2 + 30
        i = i + 1
    return sum2


# 计算当前月份天数
def current_day(year, month):
    day = 0
    if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
        day = 31
    elif month == 2:
        if is_leap_year(year):
            day = 29
        else:
            day = 28
    else:
        day = 30
    return day


# 计算每个月第一周需要空出的间隔
def gap(total):
    week = (total + 1) % 7  # 间隔总数
    # print(week)
    count = 0
    i = 1
    while i <= week:
        i = i + 1
        print("\t", end='')
        count = count + 1
        if count % 7 == 0:
            print()
    return count


# 输出当月日期
def c_calender(year, month, total):
    s = current_day(year, month)
    day = 1
    count = gap(total)
    while day <= s:
        print(day, '\t', end='')
        day = day + 1
        count = count + 1
        if count % 7 == 0:
            print()


if __name__ == '__main__':
    year = int(input('请输入年份：'))
    month = int(input('请输入月份：'))
    sum1 = sum_year_day(year)
    sum2 = sum_month_day(year, month)
    total = sum1 + sum2
    print("Sun\tMon\tTue\tWed\tThu\tFir\tSat")
    c_calender(year, month, total)
