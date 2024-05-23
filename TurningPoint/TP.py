'''
TP calc takes 3 inputs in the form of ax^2 + bx + c
where A, B, C are inputs.

The calc returns the quadractics in the Turining point 
form (Complete the square form) a(x + b)^2 + c, and gives
the Minimum / Maximum for the parabola
'''

def findtp(a : float, b : float, c : float) -> None:
    coef : float = a
    negxnum : float = b
    negxden : float = 2 * coef
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
        a : str = str(input("Again? y/n\n"))
        if (a == 'y'):
            findtp(int(input("int a: ")), int(input("int b: ")), float(input("int c: ")))
    except ValueError:
        print("bro huh")
    
try:
    a = float(input("int a: "))
    b = float(input("int b: "))
    c = float(input("int c: "))
    findtp(a, b, c)
except ValueError:
    print("bro what")