import calendar

date = input().split(" ")
month = int(date[0])
day = int(date[1])
year = int(date[2])

result = calendar.weekday(year, month, day)
weekdays = ["Monday", "Tuesday", "Wednesday", "Thrusday", "Friday", "Saturday", "Sunday"]
print(weekdays[result].upper())
