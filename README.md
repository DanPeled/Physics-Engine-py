# Py Physics Engine

<p>This is a physics engine designed to simulate the movement of balls in a 2D space. It uses the Python Turtle library to create a visual representation of the balls and their movement.</p><h2>Features</h2><ul><li>Allows customization of the ground height, screen width, screen height, and maximum height a ball can reach</li><li>Simulates the effects of gravity on the movement of the balls</li><li>Detects collisions between balls and the ground, reflecting their velocities accordingly</li><li>Detects collisions between balls, reflecting their velocities accordingly</li></ul><h2>Usage</h2><p>To use the physics engine, import the required libraries and create a ground and ball object. You can customize the parameters of the ground and ball objects as needed. Then, in a loop, call the <code>move</code> method of each ball object to update its position based on the laws of physics.</p><p>Example usage:</p>

```python
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
```
