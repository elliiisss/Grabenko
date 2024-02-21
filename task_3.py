year = int(input("введите год "))
if (year % 4 == 0) and (year % 100 != 0):
    print("Год", year, "- високосный")
else:
    print("Это год не високосный")