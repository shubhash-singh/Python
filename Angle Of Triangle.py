import math

p = int(input())
b= int(input())

result = math.atan2(p,b)
result = math.degrees(result)

print(f"{round(result)}\u00b0")
