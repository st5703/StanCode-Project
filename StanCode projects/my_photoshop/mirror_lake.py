"""
File: mirror_lake.py
Name: Che-Hsien, Chiu
----------------------------------
This file reads in mt-rainier.jpg and
makes a new image that creates a mirror
lake vibe by placing the inverse image of
mt-rainier.jpg below the original one
"""
from simpleimage import SimpleImage


def reflect(filename):
    """
    :param filename: string
    :return: SimpleImage
    """
    img = SimpleImage(filename)
    new_img = SimpleImage.blank(img.width, img.height * 2)
    for y in range(img.height):
        for x in range(img.width):
            pixel = img.get_pixel(x,y)

            upper_img = new_img.get_pixel(x,y)
            lower_img = new_img.get_pixel(x,new_img.height-y-1)

            upper_img.red = pixel.red
            upper_img.green = pixel.green
            upper_img.blue = pixel.blue

            lower_img.red = pixel.red
            lower_img.green = pixel.green
            lower_img.blue = pixel.blue

    return new_img


def main():
    """
    mirror an image
    """
    original_mt = SimpleImage('images/mt-rainier.jpg')
    original_mt.show()
    reflected = reflect('images/mt-rainier.jpg')
    reflected.show()


if __name__ == '__main__':
    main()
