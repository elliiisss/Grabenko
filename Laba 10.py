def task1():
    import json

    with open("products.json", "r") as file:
        data = json.load(file)

    for product in data["products"]:
        print(f"Название: {product['name']}")
        print(f"Цена: {product['price']}")
        print(f"Вес: {product['weight']}")
        print("В наличии") if product.get("available") else print("Нет Нет в наличии!")
        print()


def task2():
    import json

    def add_product():
        name = input("Введите название продукта: ")
        price = int(input("Введите цену продукта: "))
        weight = float(input("Введите вес продукта: "))
        available = input("Введите доступность продукта (да/нет): ").lower() == "да"

        new_product = {"name": name, "price": price, "weight": weight, "available": available}

        with open("products.json", "r") as file:
            data = json.load(file)

        data["products"].append(new_product)

        with open("products.json", "w") as file:
            json.dump(data, file, indent=4)

        print("Продукт успешно добавлен!")

    def print_products():
        with open("products.json", "r") as file:
            data = json.load(file)

        for product in data["products"]:
            print(f"Название: {product['name']}")
            print(f"Цена: {product['price']} руб.")
            print(f"Вес: {product['weight']} кг.")
            print("В наличии") if product.get("available") else print("Нет в наличии!")
            print()

    while True:
        choice = input("Выберите действие:\n1. Добавить продукт\n2. Вывести список продуктов\n0. Выход\n")

        if choice == "1":
            add_product()
        elif choice == "2":
            print_products()
        elif choice == "0":
            break
        else:
            print("Неверный выбор. Повторите попытку.")


def task3():
    def translate_file(input_file, output_file):
        with open(input_file, "r") as f_in, open(output_file, "a") as f_out:
            for line in f_in.readlines():
                less = line.split(" - ")
                f_out.write(f"{less[1][:(len(less[1]) - 1)]} - {less[0]}\n") if less[1].endswith("\n") else f_out.write(
                    f"{less[1]} - {less[0]}")

    input_file = "en-ru.txt"  # название файла с англо-русским словарем
    output_file = "ru-en.txt"  # названия файла в котором будет записан русско-английский словарь

    translate_file(input_file, output_file)

    print(f"Перевод слов из {input_file} в {output_file} выполнен!")