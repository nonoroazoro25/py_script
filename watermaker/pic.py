# -*- coding: utf-8 -*-

# 适合文字，底色为白色的
from PIL import Image
from itertools import product


def remove_img():
    image_file = r"D:\pic1_2.PNG"

    img = Image.open(image_file)
    width, height = img.size

    for pos in product(range(width), range(height)):
        rgb = img.getpixel(pos)[:3]
        if sum(rgb) >= 600:
            img.putpixel(pos, (255, 255, 255))
    img.save('d:/1.png')


remove_img()
