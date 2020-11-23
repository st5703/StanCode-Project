"""
File: babygraphics.py
Name: Che-Hsien, Chiu

SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.

baby name statistics in each year
"""

import tkinter
import babynames
import babygraphicsgui as gui

FILENAMES = [
    'data/full/baby-1900.txt', 'data/full/baby-1910.txt',
    'data/full/baby-1920.txt', 'data/full/baby-1930.txt',
    'data/full/baby-1940.txt', 'data/full/baby-1950.txt',
    'data/full/baby-1960.txt', 'data/full/baby-1970.txt',
    'data/full/baby-1980.txt', 'data/full/baby-1990.txt',
    'data/full/baby-2000.txt', 'data/full/baby-2010.txt'
]
CANVAS_WIDTH = 1000
CANVAS_HEIGHT = 600
YEARS = [1900, 1910, 1920, 1930, 1940, 1950, 1960, 1970, 1980, 1990, 2000, 2010]
GRAPH_MARGIN_SIZE = 20
COLORS = ['red', 'purple', 'green', 'blue']
TEXT_DX = 2
LINE_WIDTH = 2
MAX_RANK = 1000


def get_x_coordinate(width, year_index):
    """
    Given the width of the canvas and the index of the current year
    in the YEARS list, returns the x coordinate of the vertical
    line associated with that year.

    Input:
        width (int): The width of the canvas
        year_index (int): The index of the current year in the YEARS list
    Returns:
        x_coordinate (int): The x coordinate of the vertical line associated
                              with the specified year.
    """
    year_count = len(YEARS)
    x_width = width-GRAPH_MARGIN_SIZE - GRAPH_MARGIN_SIZE
    x_space = x_width / year_count    # x space between each year

    return GRAPH_MARGIN_SIZE + year_index * x_space


def draw_fixed_lines(canvas):
    """
    Erases all existing information on the given canvas and then
    draws the fixed background lines on it.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.

    Returns:
        This function does not return any value.
    """
    canvas.delete('all')            # delete all existing lines from the canvas

    # Write your code below this line
    #################################
    canvas.create_line(GRAPH_MARGIN_SIZE,GRAPH_MARGIN_SIZE,CANVAS_WIDTH-GRAPH_MARGIN_SIZE,GRAPH_MARGIN_SIZE)
    canvas.create_line(GRAPH_MARGIN_SIZE, CANVAS_HEIGHT- GRAPH_MARGIN_SIZE, CANVAS_WIDTH - GRAPH_MARGIN_SIZE,\
                       CANVAS_HEIGHT- GRAPH_MARGIN_SIZE)

    for i in range(len(YEARS)):    # draw line and text in each year in YEARS
        x = get_x_coordinate(CANVAS_WIDTH, i)
        canvas.create_line(x, 0, x, GRAPH_MARGIN_SIZE+CANVAS_HEIGHT)
        canvas.create_text(x + TEXT_DX, CANVAS_HEIGHT- GRAPH_MARGIN_SIZE, text=YEARS[i], anchor=tkinter.NW)


def draw_names(canvas, name_data, lookup_names):
    """
    Given a dict of baby name data and a list of name, plots
    the historical trend of those names onto the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
        name_data (dict): Dictionary holding baby name data
        lookup_names (List[str]): A list of names whose data you want to plot

    Returns:
        This function does not return any value.
    """
    draw_fixed_lines(canvas)        # draw the fixed background grid

    # Write your code below this line
    #################################

    dy = (CANVAS_HEIGHT - 2*GRAPH_MARGIN_SIZE) / MAX_RANK    # y space between each rank
    c = 0    # color index

    for name in lookup_names:    # by each name operation
        for i in range(len(YEARS)-1):
            # check rank if out of 1000
            if str(YEARS[i]) not in name_data[name]:
                rank1 = 1001    #
            else:
                rank1 = name_data[name][str(YEARS[i])]    # rank < 1000, record rank1

            if str(YEARS[i+1]) not in name_data[name]:
                rank2 = 1001
            else:
                rank2 = name_data[name][str(YEARS[i+1])]    # rank < 1000, record rank2

            # calculate x1, y1, x2, y2 for drawing line
            y1 = GRAPH_MARGIN_SIZE + (int(rank1)-1)*dy
            y2 = GRAPH_MARGIN_SIZE + (int(rank2)-1)*dy
            x1 = get_x_coordinate(CANVAS_WIDTH, i)
            x2 = get_x_coordinate(CANVAS_WIDTH, i+1)

            # draw line
            canvas.create_line(x1, y1, x2, y2, fill=COLORS[c % len(COLORS)], width=LINE_WIDTH)

            # if rank out of 1000, show '*' at canvas
            if int(rank1) > 1000:
                canvas.create_text(x1 + TEXT_DX, y1, text=f'{name} *', anchor=tkinter.SW,\
                                   fill=COLORS[c % len(COLORS)])
            else:
                canvas.create_text(x1 + TEXT_DX, y1, text=f'{name} {rank1}', anchor=tkinter.SW,
                                   fill=COLORS[c % len(COLORS)])
            if int(rank2) > 1000:
                canvas.create_text(x2 + TEXT_DX, y2, text=f'{name} *', anchor=tkinter.SW,
                                   fill=COLORS[c % len(COLORS)])
            else:
                canvas.create_text(x2 + TEXT_DX, y2, text=f'{name} {rank2}', anchor=tkinter.SW,
                                   fill=COLORS[c % len(COLORS)])

        c += 1    # select next color in COLORS

# main() code is provided, feel free to read through it but DO NOT MODIFY
def main():
    # Load data
    name_data = babynames.read_files(FILENAMES)

    # Create the window and the canvas
    top = tkinter.Tk()
    top.wm_title('Baby Names')
    canvas = gui.make_gui(top, CANVAS_WIDTH, CANVAS_HEIGHT, name_data, draw_names, babynames.search_names)

    # Call draw_fixed_lines() once at startup so we have the lines
    # even before the user types anything.
    draw_fixed_lines(canvas)

    # This line starts the graphical loop that is responsible for
    # processing user interactions and plotting data
    top.mainloop()


if __name__ == '__main__':
    main()
