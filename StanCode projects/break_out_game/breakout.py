"""
File: breakout.py
Name: Che-Hsien, Chiu

stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao

User side of Breakout Project
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics


FRAME_RATE = 1000 / 120    # 120 frames per second.
NUM_LIVES = 3


def main():
    graphics = BreakoutGraphics()

    # Add animation loop here!
    for i in range(NUM_LIVES):
        graphics.wait_click()    # wait start
        while True:
            dx = graphics.get_dx()    # update dx every loop
            dy = graphics.get_dy()    # update dy every loop
            graphics.ball.move(dx, dy)
            pause(FRAME_RATE)

            # rebound at boundary
            if graphics.ball.y < 0 :
                graphics.vertical_rebound()
            if graphics.ball.x + graphics.ball.width > graphics.window.width or \
                    graphics.ball.x < 0 :
                graphics.horizontal_rebound()

            # game over and reset
            if graphics.ball.y > graphics.window.height:
                graphics.reset_game_setting()
                break

            # no bricks remain, win
            if graphics.brick_number == 0:
                graphics.reset_game_setting()
                return

            # check collision
            graphics.paddle_collision()
            graphics.brick_collision()




if __name__ == '__main__':
    main()
