"""
File: shrink.py
Name: Che-Hsien, Chiu
-------------------------------
Create a new "out" image half the width and height of the original.
Set pixels at x=0 1 2 3 in out , from x=0 2 4 6 in original,
and likewise in the y direction.
"""

from simpleimage import SimpleImage


def shrink(filename):
    """
    :param filename: str,
    :return img: SimpleImage,
    """
    img = SimpleImage(filename)
    new_img = SimpleImage.blank(img.width //2, img.height//2)
    for y in range(img.height):
        for x in range(img.width):
            pixel = img.get_pixel(x,y)
            new_pixel = new_img.get_pixel(x//2,y//2)    # choose 1 pixel replace 4x4 pixel
            new_pixel.red = pixel.red
            new_pixel.blue = pixel.blue
            new_pixel.green = pixel.green

    return new_img


def main():
    """
    shrink image
    """
    original = SimpleImage("images/poppy.png")
    original.show()
    after_shrink = shrink("images/poppy.png")
    after_shrink.show()


if __name__ == '__main__':
    main()
