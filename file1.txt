import math

x = int(input("Введите значение x:"))
y = int(input("Введите значение y:"))
z = int(input("Введите значение z:"))
m = int(input("Введите значение m:"))
a = int(input("Введите значение a:"))
b = float(input("Введите значение b:"))
c = float(input("Введите значение c:"))

primer = (x*y*z*math.sqrt(m))/(math.fabs(a)*(b*c))

print(primer)