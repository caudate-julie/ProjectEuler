# How many Sundays fell on the first of the month
# during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

# 1 Jan 1900 was a Monday
STYEAR = 1906
MONTH = [0, 1, -1, 0, 0, 1, 1, 2, 3, 3, 4, 4]

def DaysGone(date, month, year):
    days = 0
    days += (year - STYEAR)*365 + (year - STYEAR)/4
    days += (month-1)*30 + MONTH[month-1]
    if month > 2 and year%4 == 0 and (year%100 != 0 or year%400 == 0):
        days += 1
    days += date
    return days

def Sundays1(maxyear):
    mondays = 0
    for year in range(STYEAR, maxyear):
        for month in range(1, 13):
            if DaysGone(1, month, year)%7 == 0:
                mondays += 1
    return mondays

def LeapYears(yearpair):
    y1 = min(yearpair)
    y2 = max(yearpair) - 1
    y1 -= y1%4
    res = (y2 - y1)/4
    t = y2/100 - y1/100
    if t != 0:
        res -= t
    t = y2/400 - y1/400
    if t != 0:
        res += t
    return res

def DaysPassed((day1, month1, year1), (day2, month2, year2)):
# we consider date1 < date2
    days = 0
    days += (year2 - year1)*365 + LeapYears((year1, year2))
    days -= (month1-1)*30 + MONTH[month1-1]
    days += (month2-1)*30 + MONTH[month2-1]
    if month2 > 2 and LeapYears((year2-1, year2+1)) != 0:
        days += 1
    if month1 < 3 and LeapYears((year1-1, year1+1)) != 0:
        days += 1
    if month1 == 2 and day1 == 29:
        days -= 1 
    days += - day1 + day2
    return days

def SameCycle (cycle, d, m, year):
    prevyear = year - 1
    while True:
        if DaysPassed((d, m, prevyear),(d, m, year))%cycle == 0:
            return prevyear
        prevyear -= 1

print SameCycle (59, 31, 10, 1944)
            
