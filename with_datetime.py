from Calendar import Calendar
import datetime

dateIsCorrect = None
year = Calendar.get_year()
month = Calendar.get_month()
day = Calendar.get_day()

try:
    newDate = datetime.datetime(year, month, day)
    dateValid = True
except ValueError:
    dateValid = False

print(str(year) + ' ' + str(month) + ' ' + str(day) + ' This is ' + ('' if dateValid else 'NOT ') + 'grisha\'s calendar date')
