"""
Name: Stephanie Pittman
three_door_game.py

Problem: Develop a Python program that uses numeric data from a text file.
         Create a new text file with the correct format.

Certificate of Authenticity:
I certify that this assignment is my work and was discussed with Tutor Brooke Duvall.

"""

from graphics import Text, Point, GraphWin, Rectangle
from button import Button
from random import randint

def main():

    win = GraphWin("Three Door Game", 500, 500)
    win.setCoords(0, 0, 10, 10)

    win.setBackground('white')

    open_text = Text(Point(5, 9), "I have a secret door")
    open_text.draw(win)
    secret = Text(Point(5, 2), "Click to choose my door.")
    secret.draw(win)

    widget = Rectangle(Point(2, 4), Point(4, 7))
    widget_2 = Rectangle(Point(4, 4), Point(6, 7))
    widget_3 = Rectangle(Point(6, 4), Point(8, 7))

    door_1 = Button(widget, "Door 1")
    door_1.draw(win)
    door_2 = Button(widget_2, "Door 2")
    door_2.draw(win)
    door_3 = Button(widget_3, "Door 3")
    door_3.draw(win)

    choice = randint(1, 3)
    point = win.getMouse()

    while not door_1.is_clicked(point) and not door_2.is_clicked(point) and not door_3.is_clicked(point):
        point = win.getMouse()
        
    clicked_door = 0

    if door_1.is_clicked(point):
        clicked_door = 1
    elif door_2.is_clicked(point):
        clicked_door = 2
    elif door_3.is_clicked(point):
        clicked_door = 3

    if choice == clicked_door:
        if choice == 1:
            door_1.color_button('green')
        elif choice == 2:
            door_2.color_button('green')
        elif choice == 3:
            door_3.color_button('green')
        open_text.setText("You Win!")
        secret.setText("Click to close")
    else:
        if clicked_door == 1:
            door_1.color_button('red')
        elif clicked_door == 2:
            door_2.color_button('red')
        elif clicked_door == 3:
            door_3.color_button('red')
        open_text.setText("You lost!")
        secret.setText("My secret door is " + str(choice))

    win.getMouse()


if __name__ == '__main__':
    main()
