from physics import *
import random as rnd
# Create a list of balls
balls = []
balls.append(Ball(-50, 100, 3, 'red', 1.5, 1.5))
balls.append(Ball(50, 150, -3, 'blue', 1.5, 1.5))

# Create a ground object
ground = Ground(-300, GROUND_Y)

# Simulation parameters
gravity = 9.8
dt = 0.1
counter = 0
while True:
    # Update ball positions and check for collisions
    for ball in balls:
        ball.turtle.down()
        ball.move(gravity, dt)
        if counter == 60:
            for ball_ in balls:
                ball_.turtle.pencolor(rnd.randint(
                    0, 255), rnd.randint(0, 255), rnd.randint(0, 255))
            counter = 0
    counter += 1
    # Update turtle screen
    wn.update()
