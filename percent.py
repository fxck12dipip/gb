n = 0
a = [2, 3, 4]

while n != 100:
    n += 1
    if n in (11, 12, 13, 14):
        print(n, 'процентов')

    elif n == 1 or n % 10 == 1:
        print(n, 'процент')

    elif n in (2, 3, 4) or n % 10 in (2, 3, 4):
        print(n, 'процента')

    elif n in (11, 12, 13, 14):
        print(n, 'процентов')
    else:
        print(n, 'процентов')
