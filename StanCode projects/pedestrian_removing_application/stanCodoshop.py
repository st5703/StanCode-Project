"""
File: stanCodoshop.py
----------------------------------------------
SC101_Assignment3
Adapted from Nick Parlante's
Ghost assignment by Jerry Liao.

-----------------------------------------------

TODO: remove people from picture
"""

import os
import sys
from simpleimage import SimpleImage
import math


def get_pixel_dist(pixel, red, green, blue):
    """
    Returns the color distance between pixel and mean RGB value

    Input:
        pixel (Pixel): pixel with RGB values to be compared
        red (int): average red value across all images
        green (int): average green value across all images
        blue (int): average blue value across all images

    Returns:
        dist (int): color distance between red, green, and blue pixel values

    """
    color_dis_square = (pixel.red - red)**2 + (pixel.green - green)**2 + (pixel.blue - blue)**2
    color_dis = math.sqrt(color_dis_square)
    return color_dis


def get_average(pixels):
    """
    Given a list of pixels, finds the average red, blue, and green values

    Input:
        pixels (List[Pixel]): list of pixels to be averaged
    Returns:
        rgb (List[int]): list of average red, green, blue values across pixels respectively

    Assumes you are returning in the order: [red, green, blue]

    """
    number = len(pixels)    # number of picture N
    sum_red = 0
    sum_green = 0
    sum_blue = 0

    for i in pixels:
        sum_red += i.red
        sum_green += i.green
        sum_blue += i.blue
    return [sum_red//number, sum_green//number, sum_blue//number]





def get_best_pixel(pixels):
    """
    Given a list of pixels, returns the pixel with the smallest
    distance from the average red, green, and blue values across all pixels.

    Input:
        pixels (List[Pixel]): list of pixels to be averaged and compared
    Returns:
        best (Pixel): pixel closest to RGB averages

    """
    avg_pixel = get_average(pixels)
    min_dis = 9999999999
    min_pixel = None
    # check each items in pixels to find the closest pixel
    for i in pixels:
        dis = get_pixel_dist(i, avg_pixel[0], avg_pixel[1], avg_pixel[2])
        if dis < min_dis:
            min_pixel = i
            min_dis = dis
    return min_pixel



def solve(images):
    """
    Given a list of image objects, compute and display a Ghost solution image
    based on these images. There will be at least 3 images and they will all
    be the same size.

    Input:
        images (List[SimpleImage]): list of images to be processed
    """
    width = images[0].width
    height = images[0].height
    result = SimpleImage.blank(width, height)
    ######## YOUR CODE STARTS HERE #########

    # modify each pixel in result image
    for y in range(height):
        for x in range(width):
            img_pixel = []    # create a empty list
            for i in images:
                img_pixel.append(i.get_pixel(x,y))    # add pixel at (x,y) from each image
            best_pixel = get_best_pixel(img_pixel)    # find to best image
            result_pixel = result.get_pixel(x,y)    # get pixel from result image at (x,y)
            result_pixel.red = best_pixel.red   # modify red pixel in result image
            result_pixel.green = best_pixel.green   # modify green pixel in result image
            result_pixel.blue = best_pixel.blue    # modify blue pixel in result image

    ######## YOUR CODE ENDS HERE ###########
    print("Displaying image!")
    result.show()


def jpgs_in_dir(dir):
    """
    (provided, DO NOT MODIFY)
    Given the name of a directory, returns a list of the .jpg filenames
    within it.

    Input:
        dir (string): name of directory
    Returns:
        filenames(List[string]): names of jpg files in directory
    """
    filenames = []
    for filename in os.listdir(dir):
        if filename.endswith('.jpg'):
            filenames.append(os.path.join(dir, filename))
    return filenames


def load_images(dir):
    """
    (provided, DO NOT MODIFY)
    Given a directory name, reads all the .jpg files within it into memory and
    returns them in a list. Prints the filenames out as it goes.

    Input:
        dir (string): name of directory
    Returns:
        images (List[SimpleImages]): list of images in directory
    """
    images = []
    jpgs = jpgs_in_dir(dir)
    for filename in jpgs:
        print("Loading", filename)
        image = SimpleImage(filename)
        images.append(image)
    return images


def main():
    # (provided, DO NOT MODIFY)
    args = sys.argv[1:]
    # We just take 1 argument, the folder containing all the images.
    # The load_images() capability is provided above.
    images = load_images(args[0])
    solve(images)


if __name__ == '__main__':
    main()
