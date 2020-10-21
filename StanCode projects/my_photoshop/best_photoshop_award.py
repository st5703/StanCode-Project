"""
File: best_photoshop_award.py
Name: Che-Hsien, Chiu
----------------------------------
This file creates a photoshopped image
that is going to compete for the 2020 Best
Photoshop Award for SC101P.
Please put all the images you use in image_contest folder
and make sure to choose which award you are aiming at
"""
from simpleimage import SimpleImage

# Constants
THRESHOLD = 1.3     # Controls the threshold of detecting green screen pixel
BLACK_PIXEL = 120   # Controls the upper bound for black pixel


def combine(back, me):
    """
    : param1 back: SimpleImage, the background image
    : param2 ma: SimpleImage, green screen figure image
    : return me: SimpleImage, me image with the green screen pixels replaced by pixels of back
    """
    for y in range(back.height):
        for x in range(back.width):
            pixel_me = me.get_pixel(x, y)
            avg = (pixel_me.red+pixel_me.blue+pixel_me.green) // 3
            total = pixel_me.red+pixel_me.blue+pixel_me.green
            if pixel_me.green > avg*THRESHOLD and total > BLACK_PIXEL:
                pixel_bg = back.get_pixel(x, y)
                pixel_me.red = pixel_bg.red
                pixel_me.blue = pixel_bg.blue
                pixel_me.green = pixel_bg.green
    return me



def main():
    """
    combine two pictures
    """
    me = SimpleImage("image_contest/me5.png")

    background_img = SimpleImage("image_contest/hp.jpg")

    # create a same width*height as background_img
    new_me = SimpleImage.blank(background_img.width,background_img.height)

    # shift me to right side
    for y in range(me.height):
        for x in range(me.width):
            pixel = me.get_pixel(x,y)
            new_pixel = new_me.get_pixel(x+new_me.width-me.width,y+new_me.height-me.height)
            new_pixel.red = pixel.red
            new_pixel.blue = pixel.blue
            new_pixel.green = pixel.green

    # new create space filled with green
    for p in new_me:
        if p.red == 255 and p.green == 255 and p.blue == 255:
            p.red = 0
            p.blue = 0

    combine(background_img,new_me)
    new_me.show()

if __name__ == '__main__':
    main()
