"""
Name: Stephanie Pittman
button.py

Problem: Develop a Python program that uses numeric data from a text file.
         Create a new text file with the correct format.

Certificate of Authenticity:
I certify that this assignment is my work and was discussed with Tutor Brooke Duvall.

"""
from graphics import *


class Button:
    def __init__(self, rectangle_shape, string_label):

        self.rectangle_shape = rectangle_shape

        center = self.rectangle_shape.getCenter()
        self.rectangle_shape.setFill('white')

        self.string_label = Text(center, string_label)

    def draw(self, win):
        self.rectangle_shape.draw(win)
        self.string_label.draw(win)

    def undraw(self):
        self.rectangle_shape.undraw()
        self.string_label.undraw()

    def is_clicked(self, point):
        return self.rectangle_shape.getP1().getX() <= point.getX() <= self.rectangle_shape.getP2().getX() and \
        self.rectangle_shape.getP1().getY() <= point.getY() <= self.rectangle_shape.getP2().getY()

    def get_label(self):
        return self.string_label.getText()

    def color_button(self, color):
        self.rectangle_shape.setFill(color)






