def task1():
    from PIL import Image
    image = Image.open('кчау.jpg')
    image.show()
    cropped = image.crop((0, 250, 750, 618))
    cropped.show()
    cropped.save('cropped_kchay.jpg')

def task2():
    from PIL import Image
    holiday = {'День рождения': 'др.jpg', '8 марта': '8.jpg', 'Новый год': 'нг.jpg', 'День Святого валентина': '14.jpg'}
    a = input('Открытка к какому празднику вам нужна?')
    if a in holiday:
        card = holiday[a]
        print(f"Открытка к празднику '{a}':")

        card_image = Image.open(card)
        card_image.show()
    else:
        print("Открытка не найдена")

def task3():
    from PIL import Image, ImageDraw, ImageFont
    b = input("Введите имя человеку, которому хотите отправить открытку")
    holiday = {'День рождения': 'др.jpg', '8 марта': '8.jpg', 'Новый год': 'нг.jpg', 'День Святого валентина': '14.jpg'}
    a = input('Открытка к какому празднику вам нужна?')
    if a in holiday:
        card = holiday[a]
        print(f"Открытка к празднику '{a}':")

        card_image = Image.open(card)
        font = ImageFont.truetype("arial.ttf", 25)
        dr = ImageDraw.Draw(card_image)
        dr.text((50, 18), b, font = font, fill = 'red')
        dr.text((105, 18), ", поздравляю!", font = font, fill = 'blue')
        card_image.show()
        card_image.save('new.png')
    else:
        print("Открытка не найдена")
task3()
