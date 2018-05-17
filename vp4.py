# COPYRIGHT 2018 BY LARRY TSENG
#

from deck import *
from handEval import *
from graphics import *
from Button import Button
from Betting import bet


class VP4(object):

    def __init__(self):

        self.window = GraphWin('Poker', 400, 200)

        self.dealButton = Button(self.window, Point(50, 150), Point(100, 180), "Deal", self.prepareBet)
        self.quitButton = Button(self.window, Point(140, 150), Point(190, 180), "Quit", self.quitPoker)

        self.balance = 100
        self.balance_text = Text(Point(300, 125), "Balance: $" + str(self.balance))
        self.balance_text.draw(self.window)

        Text(Point(300, 145), "Enter a bet:").draw(self.window)

        self.betEntry = Entry(Point(300, 170), 20)
        self.betEntry.setText("")
        self.betEntry.draw(self.window)

    def prepareBet(self):
        try:
            calculation = bet(self.balance, int(self.betEntry.getText()))
        except ValueError:
            return

        if calculation == -1:
            self.betEntry.setText("Not enough money!")
            return
        else:
            self.balance = calculation
            self.displayBalance(self.balance)
            drawHand(self.window)

    def displayBalance(self, value):
        self.balance_text.setText("Balance: $" + str(value))

    def quitPoker(self):
        # type: () -> None
        """

        """
        self.window.close()
        exit()


def drawHand(window):
    # type: () -> None
    """

    """
    # get cards
    deck = Deck()
    deck.shuffle()
    hand = deck.deal(5)

    # clear screen
    for item in window.items[7:]:  # grabs all items in the window (except for buttons/entry/text)
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
    Text(Point(300, 70), "High Card: " + str(high_value)).draw(window)


vp4 = VP4()

while True:
    click = vp4.window.getMouse()
    vp4.dealButton.onTarget(click)
    vp4.quitButton.onTarget(click)
