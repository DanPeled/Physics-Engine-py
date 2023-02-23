import turtle as tr
import math
tr.colormode(255)

wn = tr.Screen()
wn.tracer(0)  # turn off turtle screen updates

GROUND_Y = -200  # Customize the y coordinate of the ground
SCREEN_WIDTH = 800  # Customize the width of the screen
SCREEN_HEIGHT = 600  # Customize the height of the screen
MAX_HEIGHT = 400  # Customize the maximum height a ball can reach

# Create a ground object


class Ground:
    def __init__(self, x, y):
        self.ground = tr.Turtle()
        self.ground.speed(0)
        self.ground.up()
        self.ground.goto(x, y)
        self.ground.down()
        self.ground.color('green')
        self.ground.begin_fill()
        self.ground.goto(300, y)
        self.ground.goto(300, y - 10)
        self.ground.goto(x - 10, y - 10)
        self.ground.goto(x - 10, y)
        self.ground.end_fill()

# Create a Ball object


class Ball:
    def __init__(self, x, y, radius, color, dx, dy):
        self.turtle = tr.Turtle(shape="circle")
        self.turtle.up()
        self.turtle.goto(x, y)
        self.turtle.shapesize(radius)
        self.turtle.color(color)
        self.dx = dx
        self.dy = dy

    def move(self, gravity, dt):
        x, y = self.turtle.position()
        new_x = x + self.dx
        new_y = y + self.dy

        # Check the x boundaries
        if new_x >= SCREEN_WIDTH / 2 - self.turtle.shapesize()[0] * 10:
            self.dx = -self.dx
            new_x = SCREEN_WIDTH / 2 - self.turtle.shapesize()[0] * 10
        elif new_x <= -SCREEN_WIDTH / 2 + self.turtle.shapesize()[0] * 10:
            self.dx = -self.dx
            new_x = -SCREEN_WIDTH / 2 + self.turtle.shapesize()[0] * 10

        # Check the y boundaries
        if new_y >= MAX_HEIGHT - self.turtle.shapesize()[0] * 10:
            self.dy = -self.dy
            new_y = MAX_HEIGHT - self.turtle.shapesize()[0] * 10
        elif new_y <= GROUND_Y + self.turtle.shapesize()[0] * 10:
            # If the ball would intersect with the ground, reflect its y-velocity
            self.dy = -self.dy
            new_y = GROUND_Y + self.turtle.shapesize()[0] * 10

        self.turtle.goto(new_x, new_y)
