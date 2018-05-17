# COPYRIGHT 2018 BY LARRY TSENG
#

from deck import *
from handEval import *
from graphics import *


class Button(object):

    def __init__(self, win, point1, point2, text, action):
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
            self.action()


def drawHand():
    # type: () -> None
    """

    """
    # get cards
    deck = Deck()
    deck.shuffle()
    hand = deck.deal(5)

    # clear screen
    for item in window.items[4:]:  # grabs all items in the window (except for buttons/text)
        item.undraw()

    window.update()

    # set a starting point
    x = 50

    # render each card
    for card in hand:
        x += 20  # moves each successive card to the right
        point = Point(x, 80)

        # draws the card at the point described above
        i = Image(point, "cards/" + card + ".gif")
        i.draw(window)

    # report values
    types = ["high card", "pair", "2 pair", "3 of a kind",
             "straight", "flush", "full house", "4 of a kind", "straight flush"]
    values = ["2-10", "Jack", "Queen", "King", "Ace"]

    hand_text = types[handType(hand)]

    if highCard(hand) > 10:
        high_value = values[highCard(hand) - 10]
    else:
        high_value = values[0]

    Text(Point(300, 50), "Hand Type: " + str(hand_text)).draw(window)
    Text(Point(300, 90), "High Card: " + str(high_value)).draw(window)


def quitPoker():
    # type: () -> None
    """

    """
    window.close()
    exit()


window = GraphWin('Poker', 400, 200)

dealButton = Button(window, Point(50, 150), Point(100, 180), "Deal", drawHand)
quitButton = Button(window, Point(150, 150), Point(200, 180), "Quit", quitPoker)

while True:
    click = window.getMouse()
    dealButton.onTarget(click)
    quitButton.onTarget(click)
