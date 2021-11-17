"""
Author: Stephanie Pittman
CSCI 220

Certificate of Authenticity:
I hear by certify that this is my own work and I discussed this with Tutor Brooke Duvall


Input: Information from client
Output: Two circles simulating bouncing bumper cars

"""
import random
from math import sqrt
from graphics import Circle, GraphWin, color_rgb, Point, update


def get_random(move_amount):
    return random.randint(-move_amount, move_amount + 1)


def did_collide(circle_ball, circle_ball2):
    c1x = circle_ball.getCenter().getX()
    c1y = circle_ball.getCenter().getY()
    c2x = circle_ball2.getCenter().getX()
    c2y = circle_ball2.getCenter().getY()
    c1_rad = circle_ball.getRadius()
    c2_rad = circle_ball2.getRadius()
    return sqrt(((c2x - c1x) ** 2) + ((c2y - c1y) ** 2)) <= (c1_rad + c2_rad)


def hit_vertical(circle_ball, win):
    c1_y = circle_ball.getCenter().getY()
    c1_rad = circle_ball.getRadius()
    height = win.getHeight()
    return c1_y <= c1_rad or c1_y >= (height - c1_rad)


def hit_horizontal(circle_ball, win):
    c1_x = circle_ball.getCenter().getX()
    c1_rad = circle_ball.getRadius()
    width = win.getWidth()
    return c1_x <= c1_rad or c1_x >= (width - c1_rad)


def get_random_color():
    red = random.randint(0, 256)
    blue = random.randint(0, 256)
    green = random.randint(0, 256)
    return color_rgb(red, green, blue)


def bumper():
    height = 800
    width = 600

    win = GraphWin("bumper", height, width)
    cir_radius = 20

    x_horizontal1 = random.randint(cir_radius, height - cir_radius)
    y_vertical1 = random.randint(cir_radius, width - cir_radius)

    circle_ball = Circle(Point(x_horizontal1, y_vertical1), cir_radius)
    circle_ball.setFill(get_random_color())
    circle_ball.draw(win)

    x_horizontal2 = random.randint(cir_radius, height - cir_radius)
    y_vertical2 = random.randint(cir_radius, width - cir_radius)

    circle_ball2 = Circle(Point(x_horizontal2, y_vertical2), cir_radius)
    circle_ball2.setFill(get_random_color())
    circle_ball2.draw(win)

    dx_1 = get_random(10)
    dy_1 = get_random(10)
    dx_2 = get_random(10)
    dy_2 = get_random(10)

    for _ in range(100):

        circle_ball.move(dx_1, dy_1)
        circle_ball2.move(dx_2, dy_2)

        if hit_horizontal(circle_ball, win):
            dx_1 = -dx_1

        if hit_vertical(circle_ball, win):
            dy_1 = -dy_1

        if hit_horizontal(circle_ball2, win):
            dx_2 = -dx_2

        if hit_vertical(circle_ball2, win):
            dy_2 = -dy_2

        if did_collide(circle_ball, circle_ball2):
            dx_1 = -dx_1
            dy_1 = -dy_1
            dx_2 = -dx_2
            dy_2 = -dy_2

        update(100)

    win.getMouse()
    win.close()


if __name__ == '__bumper__':
    bumper()
