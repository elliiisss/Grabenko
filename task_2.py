seat = int(input("введите номер места "))
if seat > 54:
    print(ошибка)
if seat < 37:
    if seat % 2 == 0:
        print("купе, верхне")
    else:
        print("купе, нижнее")
else:
    if seat % 2 == 0:
        print("боковое, верхнее")
    else:
        print("боковое, нижнее")
