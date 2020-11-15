from PIL import Image
from tkinter import Tk, PhotoImage, Canvas, NW


def algoritm (txtname, imagename, mode, size = (960,540)):
    size = size[::-1] if format == 1 else size
    img = Image.new("RGB", size, "white")
    f = open(txtname,"r")
    data = f.read().split("\n")
    for i in range(len(data)-1):
        data[i] = data[i].split(" ")
        if mode == 1:
            img.putpixel((int(data[i][0]), int(data[i][1])), (0, 0, 0))
        else:
            img.putpixel((int(data[i][1]), 540 - int(data[i][0]) if format == 3 else int(data[i][0])), (0, 0, 0))
    img.save(f"{imagename}.png")
    return size

def program ():
    txt = input("Введіть назву файлу с датасетом. Приклад: Name.txt\n")
    image = input("Введіть назву зображення:\n")
    mode = (int(input("Режими роботи програми:\n1. Пряме відображення датасету не змінюючи координат х та у\n"
                        "2. Відображення датасету змінюючи координати місцями\n"
                        "3. Відображення датасету змінюючи координати місцями та з нормальним відображенням зображеенням\n"
                        "\nВведіть 1, 2 або 3 для вибору режиму роботи програми:\n")))
    while mode not in (1, 2, 3):
        mode = (int(input("Режими роботи програми:\n1. Пряме відображення датасету не змінюючи координат х та у\n"
                            "2. Відображення датасету змінюючи координати місцями\n"
                            "3. Відображення датасету змінюючи координати місцями та з нормальним відображенням зображеенням\n"
                            "\nВведіть 1, 2 або 3 для вибору режиму роботи програми:\n")))
    size = algoritm(txt, image, mode)
    image_input = input("Хочете продивитися фотографію? (Введіть 'Так' щоб відкрити вікно):\n")
    if image_input == "Так":
        windowMain = Tk()
        windowMain.geometry(f'{size[0]}x{size[1]}+50+50')
        ph_im = PhotoImage(file=f'{image}.png')
        canv = Canvas(windowMain, width=size[0], height=size[1])
        canv.create_image(1, 1, anchor=NW, image=ph_im)
        canv.place(x=10, y=10)
        windowMain.mainloop()
    restart = input("Хочете відобразити ще один датасет? (Введіть 'Так' щоб почати заново):\n")
    if restart == "Так":
        program()

program()