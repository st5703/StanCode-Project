"""
File: blur.py
Name: Che-Hsien, Chiu
-------------------------------
This file shows the original image first,
smiley-face.png, and then compare to its
blurred image. The blur algorithm uses the
average RGB values of a pixel's nearest neighbors
"""

from simpleimage import SimpleImage


def blur(img):
    """
    :param img: SimpleImage
    :return: SimpleImage
    """
    """
    3x3 box
    -------------
    | 1 | 2 | 3 |
    -------------
    | 4 | 5 | 6 |
    -------------
    | 7 | 8 | 9 |
    -------------
    """
    new_img = SimpleImage.blank(img.width, img.height)

    for y in range(img.height):
        for x in range(img.width):
            new_pixel = new_img.get_pixel(x, y)
            # upper right corner, 4,5,7,8,
            if y == 0 and x == img.width-1:
                pixel_4 = img.get_pixel(x-1,y)
                pixel_7 = img.get_pixel(x-1,y+1)
                pixel_8 = img.get_pixel(x,y+1)
                pixel_5 = img.get_pixel(x,y)
                new_pixel.red = (pixel_4.red + pixel_7.red + pixel_8.red + pixel_5.red) / 4
                new_pixel.blue = (pixel_4.blue + pixel_7.blue + pixel_8.blue + pixel_5.blue) / 4
                new_pixel.green = (pixel_4.green + pixel_7.green + pixel_8.green + pixel_5.green) / 4

            # lower right corner, 1,2,4,5
            elif y == img.height-1 and x == img.width-1:
                pixel_1 = img.get_pixel(x-1,y-1)
                pixel_2 = img.get_pixel(x,y-1)
                pixel_4 = img.get_pixel(x-1,y)
                pixel_5 = img.get_pixel(x,y)
                new_pixel.red = (pixel_1.red + pixel_2.red + pixel_4.red + pixel_5.red) / 4
                new_pixel.blue = (pixel_1.blue + pixel_2.blue + pixel_4.blue + pixel_5.blue) / 4
                new_pixel.green = (pixel_1.green + pixel_2.green + pixel_4.green + pixel_5.green) / 4

            # upper left corner, 5,6,8,9
            elif y == 0 and x == 0:
                pixel_6 = img.get_pixel(x+1,y)
                pixel_8 = img.get_pixel(x,y+1)
                pixel_9 = img.get_pixel(x+1,y+1)
                pixel_5 = img.get_pixel(x,y)
                new_pixel.red = (pixel_6.red + pixel_8.red + pixel_9.red + pixel_5.red) / 4
                new_pixel.blue = (pixel_6.blue + pixel_8.blue + pixel_9.blue + pixel_5.blue) / 4
                new_pixel.green = (pixel_6.green + pixel_8.green + pixel_9.green + pixel_5.green) / 4

            # lower left corner, 2,3,5,6
            elif y == img.height-1 and x == 0:
                pixel_2 = img.get_pixel(x, y-1)
                pixel_3 = img.get_pixel(x+1, y-1)
                pixel_5 = img.get_pixel(x, y)
                pixel_6 = img.get_pixel(x+1, y)
                new_pixel.red = (pixel_2.red + pixel_3.red + pixel_6.red + pixel_5.red) / 4
                new_pixel.blue = (pixel_2.blue + pixel_3.blue + pixel_6.blue + pixel_5.blue) / 4
                new_pixel.green = (pixel_2.green + pixel_3.green + pixel_6.green + pixel_5.green) / 4

            # upper edge, 4,5,6,7,8,9
            elif y == 0:
                pixel_4 = img.get_pixel(x - 1, y)
                pixel_5 = img.get_pixel(x,y)
                pixel_6 = img.get_pixel(x+1,y)
                pixel_7 = img.get_pixel(x - 1, y + 1)
                pixel_8 = img.get_pixel(x,y+1)
                pixel_9 = img.get_pixel(x+1,y+1)
                new_pixel.red = (pixel_4.red + pixel_5.red + pixel_6.red + pixel_7.red + pixel_8.red + pixel_9.red) / 6
                new_pixel.blue = (pixel_4.blue + pixel_5.blue + pixel_6.blue + pixel_7.blue + pixel_8.blue + pixel_9.blue) / 6
                new_pixel.green = (pixel_4.green + pixel_5.green + pixel_6.green + pixel_7.green + pixel_8.green + pixel_9.green) / 6

            # lower edge, 1,2,3,4,5,6
            elif y == img.width-1:
                pixel_1 = img.get_pixel(x-1,y-1)
                pixel_2 = img.get_pixel(x,y-1)
                pixel_3 = img.get_pixel(x + 1, y - 1)
                pixel_4 = img.get_pixel(x - 1, y)
                pixel_5 = img.get_pixel(x,y)
                pixel_6 = img.get_pixel(x+1,y)
                new_pixel.red = (pixel_4.red + pixel_5.red + pixel_6.red + pixel_1.red + pixel_2.red + pixel_3.red) / 6
                new_pixel.blue = (pixel_4.blue + pixel_5.blue + pixel_6.blue + pixel_1.blue + pixel_2.blue + pixel_3.blue) / 6
                new_pixel.green = (pixel_4.green + pixel_5.green + pixel_6.green + pixel_1.green + pixel_2.green + pixel_3.green) / 6

            # left edge, 2,3,5,6,8,9
            elif x == 0:
                pixel_2 = img.get_pixel(x,y-1)
                pixel_3 = img.get_pixel(x + 1, y - 1)
                pixel_5 = img.get_pixel(x,y)
                pixel_6 = img.get_pixel(x+1,y)
                pixel_8 = img.get_pixel(x,y+1)
                pixel_9 = img.get_pixel(x+1,y+1)
                new_pixel.red = (pixel_2.red + pixel_3.red + pixel_5.red + pixel_6.red + pixel_8.red + pixel_9.red) / 6
                new_pixel.blue = (pixel_2.blue + pixel_3.blue + pixel_5.blue + pixel_6.blue + pixel_8.blue + pixel_9.blue) / 6
                new_pixel.green = (pixel_2.green + pixel_3.green + pixel_5.green + pixel_6.green + pixel_8.green + pixel_9.green) / 6

            # right edge, 1,2,4,5,7,8
            elif x == img.width-1:
                pixel_1 = img.get_pixel(x-1,y-1)
                pixel_2 = img.get_pixel(x,y-1)
                pixel_4 = img.get_pixel(x - 1, y)
                pixel_5 = img.get_pixel(x, y)
                pixel_7 = img.get_pixel(x - 1, y + 1)
                pixel_8 = img.get_pixel(x, y + 1)
                new_pixel.red = (pixel_1.red + pixel_2.red + pixel_5.red + pixel_4.red + pixel_8.red + pixel_7.red) / 6
                new_pixel.blue = (pixel_1.blue + pixel_2.blue + pixel_5.blue + pixel_4.blue + pixel_8.blue + pixel_7.blue) / 6
                new_pixel.green = (pixel_1.green + pixel_2.green + pixel_5.green + pixel_4.green + pixel_8.green + pixel_7.green) / 6

            # else, middle case, 1,2,3,4,5,6,7,8,9
            else:
                pixel_1 = img.get_pixel(x - 1, y - 1)
                pixel_2 = img.get_pixel(x, y - 1)
                pixel_3 = img.get_pixel(x + 1, y - 1)
                pixel_4 = img.get_pixel(x - 1, y)
                pixel_5 = img.get_pixel(x, y)
                pixel_6 = img.get_pixel(x + 1, y)
                pixel_7 = img.get_pixel(x - 1, y + 1)
                pixel_8 = img.get_pixel(x, y + 1)
                pixel_9 = img.get_pixel(x + 1, y + 1)
                new_pixel.red = (pixel_1.red + pixel_2.red + pixel_3.red + pixel_5.red + pixel_4.red + pixel_6.red + pixel_8.red + pixel_7.red + pixel_9.red) / 9
                new_pixel.blue = (pixel_1.blue + pixel_2.blue + pixel_3.blue + pixel_5.blue + pixel_4.blue + pixel_6.blue + pixel_8.blue + pixel_7.blue + pixel_9.blue) / 9
                new_pixel.green = (pixel_1.green + pixel_2.green + pixel_3.green + pixel_5.green + pixel_4.green + pixel_6.green + pixel_8.green + pixel_7.green + pixel_9.green) / 9
    return new_img


def main():
    """
    blurred image
    """
    old_img = SimpleImage("images/smiley-face.png")
    old_img.show()

    blurred_img = blur(old_img)
    for i in range(10):
        blurred_img = blur(blurred_img)
    blurred_img.show()


if __name__ == '__main__':
    main()
