"""
File: fire.py
Name: Che-Hsien, Chiu
---------------------------------
This file contains a method called
highlight_fires which detects the
pixels that are recognized as fire
and highlights them for better observation
"""
from simpleimage import SimpleImage


HURDLE_FACTOR = 1.05


def highlight_fires(filename):
    """
    :param filename: string
    :return: SimpleImage
    """
    img = SimpleImage(filename)
    for pixel in img:
        avg = (pixel.red + pixel.blue + pixel.green) / 3
        if pixel.red > avg * HURDLE_FACTOR:
            pixel.red = 255
            pixel.blue = 0
            pixel.green = 0
        else:
            pixel.red = avg
            pixel.green = avg
            pixel.blue = avg

    return img


def main():
    """
    detect forest fire
    """
    original_fire = SimpleImage('images/greenland-fire.png')
    original_fire.show()
    highlighted_fire = highlight_fires('images/greenland-fire.png')
    highlighted_fire.show()


if __name__ == '__main__':
    main()
