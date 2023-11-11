import cmath

a = complex(input())
r, angle = cmath.polar(a)
phase = cmath.phase(a)
print(r)
print(phase)
