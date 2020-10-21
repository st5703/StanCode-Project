"""
File: bouncing_ball.py
Name: Che-Hsien, Chiu
-------------------------
TODO: bouncing ball simulation
"""

from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked

VX = 3
DELAY = 10
GRAVITY = 1
SIZE = 20
REDUCE = 0.9
START_X = 30
START_Y = 40

window = GWindow(800, 500, title='bouncing_ball.py')
ball = GOval(SIZE, SIZE)
number_of_click = 0


def main():
    """
    This program simulates a bouncing ball at (START_X, START_Y)
    that has VX as x velocity and 0 as y velocity. Each bounce reduces
    y velocity to REDUCE of itself.
    """
    ball.filled = True
    ball.fill_color = 'black'
    window.add(ball, START_X, START_Y)

    onmouseclicked(bouncing)




def bouncing(mouse):
    """
    :param mouse: information about mouse
    """

    global ball, number_of_click
    # can be executed only if running count less than 3 and the ball is at starting point
    if number_of_click < 3 and ball.x == START_X:
        number_of_click += 1
        bouncing_process()

        # restart when ball out of window
        window.remove(ball)
        window.add(ball, START_X, START_Y)



def bouncing_process():
    """
    bouncing motion function
    """
    global ball
    v0 = 0    # initial speed

    while ball.x < window.width:  # keep bouncing in the window

        # speed downward
        while ball.y < window.height - SIZE:
            v1 = v0 + GRAVITY
            delta_y = (v1 * v1 - v0 * v0) / 2 * GRAVITY  # law of motion
            ball.move(VX, delta_y)
            v0 = v1  # new initial speed is precedent post speed
            pause(DELAY)

        # changing the direction of speed and reducing the speed
        v0 = -v0 * REDUCE

        # speed upward
        while v0 < 0:
            v1 = v0 + GRAVITY
            delta_y = (v1 * v1 - v0 * v0) / 2 * GRAVITY  # law of motion
            ball.move(VX, delta_y)
            v0 = v1   # new initial speed is precedent post speed
            pause(DELAY)


if __name__ == "__main__":
    main()
