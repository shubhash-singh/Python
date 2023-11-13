from datetime import datetime

def calculate_time_delta(start_date, end_date):
    time_format = "%a %d %b %Y %H:%M:%S %z"
    datetime1 = datetime.strptime(start_date, time_format)
    datetime2 = datetime.strptime(end_date, time_format)

    time_difference_seconds = abs((datetime2 - datetime1).total_seconds())

    return time_difference_seconds

n = int(input())
for i in range(n):
    start_date_str = input()
    end_date_str = input()
    result = calculate_time_delta(start_date_str, end_date_str)
    print(int(result))

