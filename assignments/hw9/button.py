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
    def __init__(self, shape, label):

        self.shape = shape
        self.label = label

        center = self.shape.getCenter()
        self.shape.setFill('white')

        self.label = Text(center, label)

    def draw(self, win):
        self.shape.draw(win)
        self.label.draw(win)

    def undraw(self):
        self.shape.undraw()
        self.label.undraw()

    def is_clicked(self, point):
        return self.shape.getP1().getX() <= point.getX() <= self.shape.getP2().getX() and \
        self.shape.getP1().getY() <= point.getY() <= self.shape.getP2().getY()

    def get_label(self):
        return self.label.getText()

    def set_label(self, label):
        return self.label.setText(label)

    def color_button(self, color):
        self.shape.setFill(color)




