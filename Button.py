# COPYRIGHT 2018 BY LARRY TSENG
# A reusable Button class made from Rectangle and Text

from graphics import *


class Button(object):

    def __init__(self, win, point1, point2, text, action=None):
        # type: (GraphWin, Point, Point, str, function) -> None
        """
        Initializes and draws a button object in a window, given points, text, and a click function handler
        :param win: GraphWin window of the game
        :param point1: point1 for the rectangle
        :param point2: point2 for the rectangle
        :param text: text for the button
        :param action: optional onClick function handler
        """
        self.p1 = point1
        self.p2 = point2
        self.action = action

        self.rectangle = Rectangle(point1, point2)
        self.text = Text(Point((point1.getX() + point2.getX()) / 2, (point1.getY() + point2.getY()) / 2), text)

        self.rectangle.draw(win)
        self.text.draw(win)

        self.removed = False

    def onTarget(self, point):
        # type: (Point) -> bool
        """
        Checks if the mouse's click is within the Button's boundaries
        :param point: the click point of the mouse
        """
        # if it's within the rectangle's boundaries
        if self.removed:
            return False

        elif self.p1.getX() < point.getX() < self.p2.getX() and self.p1.getY() < point.getY() < self.p2.getY():
            if self.action is not None:
                self.action()

            return True

        else:
            return False

    def changeText(self, text):
        # type: (str) -> None
        """
        Changes the text of the button
        :param text: new text
        """
        self.text.setText(text)

    def changeAction(self, action=None):
        # type: (function) -> None
        """
        Changes the action of the button
        :param action: the function to execute
        """
        self.action = action

    def remove(self):
        # type: () -> None
        """
        Removes the button from the window
        """
        self.rectangle.undraw()
        self.text.undraw()
        self.removed = True
