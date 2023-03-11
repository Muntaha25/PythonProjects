a= int(input("enter the number you want: "))
b= int(input("enter the next number you want: "))
c= int(input("enter the next number you want: "))
d= int(input("enter the next number you want: "))
e= int(input("enter the next number you want: "))
f= int(input("enter the next number you want: "))

if f == 0:
 s = a + b + c + d +e
x = s/5
a = (a - x)**2
b = (b - x)**2
c = (c - x)**2
d = (d - x)**2
e = (e - x)**2

v = (a+b+c+d+e)/5

sd = (v)**0.5

print("Variance: ",v)

print("Standard Deviation: ", sd)

g = int(input("enter the next number you want: "))
if g == 0:
    s = a + b + c + d +e + f
x = s/6
a = (a - x)**2
b = (b - x)**2
c = (c - x)**2
d = (d - x)**2
e = (e - x)**2
f = (f - x)**2

v = (a+b+c+d+e+f)/6

sd = (v)**0.5

print("Variance: ",v)

print("Standard Deviation: ", sd)