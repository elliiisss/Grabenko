def task1():
    from PIL import Image, ImageFilter
    import os

    source_dir = "images"
    output_dir = "processed_images"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    def process_image(image_path):
        image = Image.open(image_path)
        filtered_image = image.filter(ImageFilter.FIND_EDGES)
        filename, extension = os.path.splitext(os.path.basename(image_path))
        output_path = os.path.join(output_dir, f"{filename}_filtered{extension}")

        filtered_image.save(output_path)

    for filename in os.listdir(source_dir):
        if filename.endswith((".jpg", ".png", ".jpeg")):
            image_path = os.path.join(source_dir, filename)
            process_image(image_path)



def task2():


def task3():
    file = open("9,3.csv", "r")

    total_amount = 0

    for i in file.readlines():
        title, count, amount = i.split(",")
        total_amount += int(amount)
        print(f"{title} - {count} шт. за {amount} руб.")
    print(f"Итоговая сумма: ${total_amount} руб.")