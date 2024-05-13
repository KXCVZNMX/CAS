#Quadractics solver needs inputs in the format of ax^2 +bx + c where a, b, c = int

from math import *

def hcf(x, y, z):
    if x < y:
        smaller = x
    elif y < x:
        smaller = y
    else:
        smaller = z
    hcf = 1
    for i in range(1, smaller+1):
        if((x % i == 0) and (y % i == 0) and (z % i == 0)):
            hcf = i 
    return hcf

a = int(input("int a: "))
b = int(input("int b: "))
c = int(input("int c: "))

d = (b ** 2) - (4 * a * c)

if d < 0:
    print("The given quadratic equation has no solution")
    quit(0)

sol1 = (-b - sqrt(d)) / (2*a)
sol2 = (-b + sqrt(d)) / (2*a)

if sol1 - int(sol1) == 0 and sol2 - int(sol2) == 0:
    print(sol1)
    print(sol2)
else:
    und = d
    und0 = round(und)
    rt = []
    coef = 1
    if und == 0:
        quit(0)
    else: 
        for i in range(2, und0):
            if und % (i ** 2) == 0:
                rt.append(i)
                und /= i ** 2
                
                for j in range(2, und0):
                    if und % (j ** 2) == 0:
                        rt.append(j)
                        und /= j ** 2
        
        for e in rt:
            coef *= e
        hcf3 = hcf(b, coef, 2 * a)
        if coef != 1.0:
            print("The root is: ")
            print(str(int((-b / hcf3))) + " ± " + 
                str(int((coef / hcf3))) + "√" + str(int(und)))
            print("----------------")
            print(int((2 * a) / hcf3))
        else:
            print("The root is: ")
            print(str(int((-b / hcf3))) + " ± " + 
                 "√" + str(int(und)))
            print("----------------")
            print(int((2 * a) / hcf3))