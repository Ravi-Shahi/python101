'''
python provides calender module to work with calender
'''
import calendar

#returns calendar of year 2023
#calendar(yeear)
cal = calendar.calendar(2023)
print(cal)

#isLeap()
isLeap = calendar.isleap(2024)
print('is leap:',isLeap)

