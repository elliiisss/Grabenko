def task1():
    s = [2,7,8,4,16,]
    a = int(input("Введите число"))
    if a in s:
        print("Поздравляю, Вы угадали число!")
    else:
        print("Нет такого числа!")
def task2:
    a = [1,4,3,7,5,7,13,24]
    l = len(a)
    for i in range (l):
        for g in range( i+1, l):
            if a[i] == a[j]:
                print("Есть уникальные элементы", a[i])
            else:
                print("Все элементы уникальны")


def task3():
    days = ("Понедельник","Вторник","Среда","Четверг","Пятница","Суббота","Воскресенье")
    a = int(input("Сколько выходных на этой неделе вы хотите"))
    b = (7 - a) + 1
    print("Ваши выходные дни:", days[-a])
    print("Ваши рабочие дни:", days[1:b])

def task4():
    group1 = ['Грабенко', 'Полонская', 'Чиркунова', 'Васильева', 'Крылов', 'Шутко', 'Байрит', 'Степаненко', 'Трубаев']
    group2 = ['Максюта', 'Розина', 'Мельников', 'Рогозный', 'Паймина', 'Сведерская', 'Балабан', 'Говердовская', 'Нагачевская', 'Бехова', 'Савельев']
