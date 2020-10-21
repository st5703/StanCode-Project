"""
File: green_screen.py
Name: Che-Hsien, Chiu
-------------------------------
This file creates a new image that uses
MillenniumFalcon.png as background and
replace the green pixels in ReyGreenScreen.png
"""

from simpleimage import SimpleImage


def combine(background_img, figure_img):
    """
    :param background_img: SimpleImage
    :param figure_img: SimpleImage
    :return: SimpleImage
    """
    for y in range(figure_img.height):
        for x in range(figure_img.width):
            pixel = figure_img.get_pixel(x,y)
            if pixel.green > max(pixel.red,pixel.blue):
                background_pixel = background_img.get_pixel(x,y)
                pixel.red = background_pixel.red
                pixel.blue = background_pixel.blue
                pixel.green = background_pixel.green
    return figure_img


def main():
    """
    combine figure image with background image
    """
    space_ship = SimpleImage("images/MillenniumFalcon.png")
    figure = SimpleImage("images/ReyGreenScreen.png")
    result = combine(space_ship, figure)
    result.show()


if __name__ == '__main__':
    main()
