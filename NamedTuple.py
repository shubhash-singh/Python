# This is a python program that takes input as in spreadsheet 
# and find the average of marks
from collections import namedtuple

std_num = int(input())
rows_name = input().split()
students = namedtuple('students', [rows_name[0], rows_name[1], rows_name[2], rows_name[3]])
total_marks = 0
for i in range(std_num):
    std_detail = input().split()
    s1 = students(std_detail[0], std_detail[1], std_detail[2], std_detail[3])
    total_marks += int(s1.MARKS)
print(total_marks/std_num)