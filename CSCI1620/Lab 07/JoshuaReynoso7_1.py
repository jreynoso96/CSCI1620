def power(x,y):
    if y == 1:
        return x
    else:
        return x * power(x,y-1)

def cat_ears(n):
    if n == 1:
        return 2
    else:
        return 2 + cat_ears(n-1)

def alien_ears(a):
    if a > 1 and a % 2 == 1:
        return 3 + alien_ears(a - 1)
    elif a > 1 and a % 2 == 0:
        return 2 + alien_ears(a - 1)
    elif a == 1:
        return 3

if (__name__ == '__main__'):
    print(power(-2,3))
    print(cat_ears(4))
    print(alien_ears(3))