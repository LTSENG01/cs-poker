from graphics import *


class Button(object):

    def __init__(self, win, point1, point2, text, action=None):
        # type: (GraphWin, Point, Point, str, function) -> None
        """

        :param win:
        :param point1:
        :param point2:
        :param text:
        :param action:
        """
        self.p1 = point1
        self.p2 = point2
        self.action = action

        self.rectangle = Rectangle(point1, point2)
        self.text = Text(Point((point1.getX() + point2.getX()) / 2, (point1.getY() + point2.getY()) / 2), text)

        self.rectangle.draw(win)
        self.text.draw(win)

    def onTarget(self, point):
        # type: (Point) -> None
        """

        :param point:
        """
        # if it's within the rectangle's boundaries
        if self.p1.getX() < point.getX() < self.p2.getX() and self.p1.getY() < point.getY() < self.p2.getY():
            if self.action is not None:
                self.action()

    def changeText(self, text):
        self.text.setText(text)

    def remove(self):
        self.rectangle.undraw()
        self.text.undraw()
