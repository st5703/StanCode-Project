"""
File: draw_line.py
Name: Che-Hsien, Chiu
-------------------------
TODO: create a draw-line function on window
"""

from campy.graphics.gobjects import GOval, GLine
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked

SIZE = 10
window = GWindow()
hole1 = GOval(SIZE, SIZE)    # global object hole
hole1_is_exist = False    # check if hole1 is exist on window


def main():
    """
    This program creates lines on an instance of GWindow class.
    There is a circle indicating the user’s first click. A line appears
    at the condition where the circle disappears as the user clicks
    on the canvas for the second time.
    """
    onmouseclicked(line)




def line(mouse):
    """
    :param mouse: information about mouse
    """
    global hole1, hole1_is_exist

    # check first click or second click
    if hole1_is_exist is False:    # first click, hole1 is not exist
        window.add(hole1, x=mouse.x - (SIZE/2), y=mouse.y - (SIZE/2))
        hole1.color = 'black'
        hole1_is_exist = True

    else:    # second click, draw line and remove hole 1 on window
        line = GLine(hole1.x + (SIZE/2), hole1.y + (SIZE/2), mouse.x, mouse.y)
        window.add(line)
        window.remove(hole1)
        hole1_is_exist = False





if __name__ == "__main__":
    main()
