'''
TP calc takes 3 inputs in the form of ax^2 + bx + c
where A, B, C are inputs.

The calc returns the quadractics in the Turining point 
form (Complete the square form) a(x + b)^2 + c, and gives
the Minimum / Maximum for the parabola
'''

def findtp(a : int, b : int, c : float) -> None:
    coef : int = a
    negxnum : int = b
    negxden : int = 2 * coef
    negx : float = negxnum / negxden
    y : float = c - (negx ** 2 * coef)
    
    print("The turning point form for the given equation is:")
    if negx >= 0 and y >= 0:
        print(f'{coef} (x + {negx})^2 + {y}')
    elif negx < 0 and y < 0:
        print(f'{coef} (x {negx})^2 {y}')
    elif negx < 0 and y >= 0:
        print(f'{coef} (x {negx})^2 + {y}')
    elif negx >= 0 and y < 0:
        print(f'{coef} (x + {negx})^2 {y}')
    print("The turning point is:")
    if negx < 0:
        print(f'({negx + abs((2 * negx))}, {y})')
    elif negx >= 0:
        print(f'(-{negx}, {y})')
    
try:
    a = int(input("int a: "))
    b = int(input("int b: "))
    c = float(input("int c: "))
    findtp(a, b, c)
except ValueError:
    print("bro what")