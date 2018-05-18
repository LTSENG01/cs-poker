# COPYRIGHT 2018 BY LARRY TSENG
# A manager for the poker game

from Button import *
from Betting import *
from handEval import *
from deck import Deck


class PokerManager(object):

    def __init__(self):
        # type: () -> None
        """
        Initializes a GraphWin window, buttons, text boxes, and an entry field
        """
        self.window = GraphWin('Poker', 400, 200)

        self.dealButton = Button(self.window, Point(25, 150), Point(100, 180), "Deal", self.prepareBet)
        self.quitButton = Button(self.window, Point(130, 150), Point(205, 180), "Quit", self.quitPoker)
        self.playAgainButton = None

        self.balance = 1000
        self.balance_text = Text(Point(300, 125), "Balance: $" + str(self.balance))
        self.balance_text.draw(self.window)

        Text(Point(300, 145), "Enter a bet:").draw(self.window)

        self.betEntry = Entry(Point(300, 170), 20)
        self.betEntry.setText("")
        self.betEntry.draw(self.window)

    def prepareBet(self):
        # type: () -> None
        """
        Takes the bet entered in the Entry field and processes it
        """
        try:  # input sanitation
            calculation = bet(self.balance, int(self.betEntry.getText()))
        except ValueError:
            self.betEntry.setText("Not a number!")
            return

        if calculation == -1:
            self.betEntry.setText("Not enough money!")
            return
        else:
            self.balance = calculation
            self.displayBalance(self.balance)
            drawHand(self)

    def displayBalance(self, value):
        # type: (int) -> None
        """
        Updates the balance text box
        :param value: value of the balance
        """
        self.balance_text.setText("Balance: $" + str(value))

    def quitPoker(self):
        # type: () -> None
        """
        Closes the graphics window and quits execution of the program
        """
        self.window.close()


def drawHand(manager):
    # type: () -> None
    """
    Deals and displays cards on the window
    """
    # get cards
    deck = Deck()
    deck.shuffle()
    hand = deck.deal(5)

    # clear screen
    for item in manager.window.items[7:]:  # grabs all items in the window (except for buttons/entry/text)
        item.undraw()

    manager.window.update()

    # set a starting point
    x = 50

    # render each card
    for card in hand:
        x += 20  # moves each successive card to the right
        point = Point(x, 80)

        # draws the card at the point described above
        i = Image(point, "cards/" + card + ".gif")
        i.draw(manager.window)

    # calculate bet winnings
    hand_type = handType(hand)
    high_card = highCard(hand)
    manager.balance += calculateWinnings(int(manager.betEntry.getText()), hand_type, high_card)
    manager.displayBalance(manager.balance)

    # report values
    types = ["high card", "pair", "2 pair", "3 of a kind",
             "straight", "flush", "full house", "4 of a kind", "straight flush", "royal flush"]
    values = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]

    hand_text = types[hand_type]

    high_value = values[high_card - 2]

    Text(Point(300, 50), "Hand Type: " + str(hand_text)).draw(manager.window)
    Text(Point(300, 70), "High Card: " + str(high_value)).draw(manager.window)

    # determine if the game is over yet
    if manager.balance == 0:
        endGame(manager)


def endGame(manager):
    # type: (PokerManager) -> None
    """
    Manages the end game stage, where a player can choose to play again or qu
    :param manager: the PokerManager object currently being used
    """
    manager.betEntry.setText("Game Over :(")
    manager.dealButton.remove()
    manager.playAgainButton = Button(manager.window, Point(25, 150), Point(100, 180), "Play Again")
