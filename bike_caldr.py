from Calendar import Calendar

dateValid= None
year = int(Calendar.get_year())
month = int(Calendar.get_month())
day = int(Calendar.get_day())
daysInMonthList = [-1,31,28,30,31,30,31,30,31,30,31,30,31]

if year % 4 == 0:
    daysInMonthList[2] = 29

try:
    if month < 1 or month > 12:
        raise ValueError('nvalid month number');
    daysInMonth = daysInMonthList[month]
    if day < 1 or day > daysInMonth:
        raise ValueError('invalid day number');
    dateValid = True
except ValueError:
    dateValid = False

print(str(year) + ' ' + str(month) + ' ' + str(day) + ' is ' + ('' if dateValid else 'This NOT ') + 'grisha\'s calendar date')
