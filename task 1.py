def task1():
    a = int(input ("Введите число: "))
    if a % 7 ==0:
        print("Число делится на 7")
    else:
        print("Число не делится на 7")


def task2():
    try:
        a = int(input("Введите число: "))
        b = 200 / a
        print(b)
    except (ValueError):
        print("Можно вводить только числа")
    except (ZeroDivisionError):
        print("На ноль делить нельзя")


def task3():
    a = input("Bедите ДД.ММ.ГГГГ: ")
    b = a.split('.')
    if int(b[0]) * int(b[1]) == int(b[2][-2:]):
        print(False)
    else:
        print(True)


def task4():
    a = input("Введите номер билета: ")
    k = len(a)
    if k % 2 ==0:
        s = len(a) // 2
        a1 = list(map(int, a[:s]))
        a2 = list(map(int, a[-s:]))
        sum1 = sum(a1)
        sum2 = sum(a2)
        if sum1 == sum2:
            print("Билет счастливый")
        else:
            print("Билет несчастливый")
    else:
        print("Номер билета введен неправильно")

