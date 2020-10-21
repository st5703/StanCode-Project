"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao

YOUR DESCRIPTION HERE
Coder side of  Breakout Project
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing.
BRICK_WIDTH = 40       # Height of a brick (in pixels).
BRICK_HEIGHT = 15      # Height of a brick (in pixels).
BRICK_ROWS = 10        # Number of rows of bricks.
BRICK_COLS = 10        # Number of columns of bricks.
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels).
BALL_RADIUS = 10       # Radius of the ball (in pixels).
PADDLE_WIDTH = 75      # Width of the paddle (in pixels).
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels). 15
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels).

INITIAL_Y_SPEED = 7.0  # Initial vertical speed for the ball.
MAX_X_SPEED = 5      # Maximum initial horizontal speed for the ball.


class BreakoutGraphics:

    def __init__(self, ball_radius = BALL_RADIUS, paddle_width = PADDLE_WIDTH,
                 paddle_height = PADDLE_HEIGHT, paddle_offset = PADDLE_OFFSET,
                 brick_rows = BRICK_ROWS, brick_cols = BRICK_COLS,
                 brick_width = BRICK_WIDTH, brick_height = BRICK_HEIGHT,
                 brick_offset = BRICK_OFFSET, brick_spacing = BRICK_SPACING,
                 title='Breakout'):

        # Create a graphical window, with some extra space.
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)

        # Create a paddle.
        self.paddle = GRect(paddle_width, paddle_height, x=self.window.width / 2 - paddle_width / 2, \
                            y=self.window.height - paddle_offset)
        self.paddle.filled = True
        self.paddle.fill_color = 'black'
        self.paddle.color = 'black'
        self.window.add(self.paddle)


        # Center a filled ball in the graphical window.
        self.ball = GOval(2*ball_radius, 2*ball_radius,x = self.window.width/2 - ball_radius,\
                          y = self.window.height/2 - ball_radius)
        self.ball.filled = True
        self.ball.fill_color = 'black'
        self.ball.color = 'black'
        self.window.add(self.ball)

        # Default initial velocity for the ball.
        self.__dy = INITIAL_Y_SPEED
        self.__dx = random.randint(1, MAX_X_SPEED)
        if random.random() > 0.5:
            self.__dx = -self.__dx

        # Initialize our mouse listeners.
        onmouseclicked(self.start)
        onmousemoved(self.reset_paddle)

        # Draw bricks.
        # creating brick array by double for loop
        for j in range(brick_cols):
            for i in range(brick_rows):
                self.brick = GRect(brick_width, brick_height, x = i * (brick_width + brick_spacing),\
                                   y = j * (brick_height + brick_spacing) + brick_offset)
                self.brick.color = 'black'
                self.brick.filled = True
                if j <= 1:
                    self.brick.fill_color = 'red'
                elif j <= 3:
                    self.brick.fill_color = 'orange'
                elif j <= 5:
                    self.brick.fill_color = 'yellow'
                elif j <= 7:
                    self.brick.fill_color = 'green'
                else:
                    self.brick.fill_color = 'blue'

                self.window.add(self.brick)

        # bricks number
        self.brick_number = brick_rows * brick_cols


    def reset_paddle(self, m):
        """
        reset paddle position
        :param m: mouse information
        """
        self.paddle.x = m.x - self.paddle.width/2

        # boundary condition
        if m.x + self.paddle.width/2 > self.window.width:
            self.paddle.x = self.window.width - self.paddle.width
        elif m.x - self.paddle.width/2 < 0:
            self.paddle.x = 0

    def get_dx(self):
        """
        get dx
        """
        return self.__dx

    def get_dy(self):
        """
        get dy
        """
        return self.__dy

    def start(self, m):
        """
        game start
        :param m: mouse information
        """
        # cab be only executed when ball is at initial point
        if self.ball.x == self.window.width / 2 - self.ball.width/2 or \
                self.ball.y == self.window.height / 2 - self.ball.width/2:
            self.__dy = INITIAL_Y_SPEED
            self.__dx = random.randint(1, MAX_X_SPEED)
            if random.random() > 0.5:
                self.__dx = -self.__dx

    def vertical_rebound(self):
        """
        vertical rebound
        """
        self.__dy = -self.__dy

    def horizontal_rebound(self):
        """
        horizontal rebound
        """
        self.__dx = -self.__dx

    def paddle_collision(self):
        """
        check if collide with paddle
        """
        # paddle collision, only rebound when ball is moving downward
        ball_bottom_1 = self.window.get_object_at(self.ball.x + self.ball.width, self.ball.y + self.ball.height)
        ball_bottom_2 = self.window.get_object_at(self.ball.x, self.ball.y + self.ball.height)
        ball_bottom_3 = self.window.get_object_at(self.ball.x, self.ball.y)
        ball_bottom_4 = self.window.get_object_at(self.ball.x + self.ball.width, self.ball.y)
        if ball_bottom_1 is self.paddle and self.__dy > 0:
            self.vertical_rebound()
        if ball_bottom_2 is self.paddle and self.__dy > 0:
            self.vertical_rebound()
        if ball_bottom_3 is self.paddle and self.__dy > 0:
            self.vertical_rebound()
        if ball_bottom_4 is self.paddle and self.__dy > 0:
            self.vertical_rebound()


    def brick_collision(self):
        """
        deal with collision condition
        """
        # ball up-side collide, remove and change direction only when collide with bricks
        obj_up = self.window.get_object_at(self.ball.x + self.ball.width/2, self.ball.y - 0.1)
        if obj_up is not None and obj_up is not self.paddle:
            self.window.remove(obj_up)
            self.vertical_rebound()
            self.brick_number -= 1

        # ball bottom collide, remove and change direction only when collide with bricks
        obj_bottom = self.window.get_object_at(self.ball.x + self.ball.width/2, self.ball.y + self.ball.width + 0.1)
        if obj_bottom is not None and obj_bottom is not self.paddle:
            self.window.remove(obj_bottom)
            self.vertical_rebound()
            self.brick_number -= 1

        # left-side collide, remove and change direction only when collide with bricks
        obj_left = self.window.get_object_at(self.ball.x - 0.1, self.ball.y + self.ball.width/2)
        if obj_left is not None and obj_left is not self.paddle:
            self.window.remove(obj_left)
            self.horizontal_rebound()
            self.brick_number -= 1

        # right-side collide, remove and change direction only when collide with bricks
        obj_right = self.window.get_object_at(self.ball.x + self.ball.width + 0.1, self.ball.y + self.ball.width/2)
        if obj_right is not None and obj_right is not self.paddle:
            self.window.remove(obj_right)
            self.horizontal_rebound()
            self.brick_number -= 1

    def reset_game_setting(self):
        """
        reset game setting for game over
        """
        # remove old ball, add new ball to initial position
        self.window.remove(self.ball)
        self.window.add(self.ball, x = self.window.width/2 - self.ball.width/2, \
                        y = self.window.height/2 - self.ball.height/2)

    def wait_click(self):
        """
        wait click to start
        """
        self.__dx = 0
        self.__dy = 0


