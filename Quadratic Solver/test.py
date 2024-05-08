def hcf(x, y, z):
    if x < y:
        smaller = x
    elif y < x:
        smaller = y
    else:
        smaller = z
    for i in range(1, smaller+1):
        if((x % i == 0) and (y % i == 0) and (z % i == 0)):
            hcf = i 
    return hcf

print(hcf(2, 3, 6))