def task1():
    a = int(input ("Введите число: "))
    if a % 7 ==0:
        print("Число делится на 7")
    else:
        print("Число не делится на 7")


def task2():
    try:
        a = int(input("Введите число"))
        b = 200 / a
        print(b)
    except (ValueError):
        print("Можно вводить только числа")
    except (ZeroDivisionError):
        print("На ноль делить нельзя")


def task3():
    a = input("")
    b = a.split('.')
    if int(b[0]) * int(b[1]) == int(b[2][-2:]):
        print("")
    else:
        print("")


def task4():
    a = input("")
    k = len(a)
    if k % 2 ==0:
        s = int(lrn)


