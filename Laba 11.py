def task1():
    class Restaurant:
        def __init__(self, restaurant_name, cuisine_type):
            self.restaurant_name = restaurant_name
            self.cuisine_type = cuisine_type

        def describe_restaurant(self):
            print(f"Название ресторана: {self.restaurant_name}")
            print(f"Тип кухни: {self.cuisine_type}")

        def open_restaurant(self):
            print(f"{self.restaurant_name} открыт!")

    newRestaurant = Restaurant("Тан жён", "Китайская")

    print(f"Название ресторана: {newRestaurant.restaurant_name}")
    print(f"Тип кухни: {newRestaurant.cuisine_type}")

    newRestaurant.describe_restaurant()
    newRestaurant.open_restaurant()

def task2():
    class Restaurant:
        def __init__(self, restaurant_name, cuisine_type):
            self.restaurant_name = restaurant_name
            self.cuisine_type = cuisine_type

        def describe_restaurant(self):
            print(f"Название ресторана: {self.restaurant_name}")
            print(f"Тип кухни: {self.cuisine_type}")

    restaurant1 = Restaurant("Уютное место", "Европейская")
    restaurant2 = Restaurant("Суши-бар", "Японская")
    restaurant3 = Restaurant("Пицца и паста", "Итальянская")

    restaurant1.describe_restaurant()
    restaurant2.describe_restaurant()
    restaurant3.describe_restaurant()


def task3():
    class Restaurant:
        def __init__(self, restaurant_name, cuisine_type, rating=0):
            self.restaurant_name = restaurant_name
            self.cuisine_type = cuisine_type
            self.rating = rating

        def describe_restaurant(self):
            print(f"Название ресторана: {self.restaurant_name}")
            print(f"Тип кухни: {self.cuisine_type}")
            print(f"Рейтинг: {self.rating}")

        def update_rating(self, new_rating):
            if new_rating >= 0:
                self.rating = new_rating
                print(f"Рейтинг {self.restaurant_name} обновлен до {self.rating}")
            else:
                print(f"Ошибка: новое значение рейтинга должно быть неотрицательным.")

    restaurant1 = Restaurant("Уютное место", "Европейская", 4.5)
    restaurant2 = Restaurant("Суши-бар", "Японская", 5)
    restaurant3 = Restaurant("Пицца и паста", "Итальянская", 3.8)

    restaurant1.describe_restaurant()
    restaurant1.update_rating(4.7)

    restaurant2.describe_restaurant()
    restaurant2.update_rating(-1)  # Ошибка

    restaurant3.describe_restaurant()
    restaurant3.update_rating(4.2)

