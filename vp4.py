# COPYRIGHT 2018 BY LARRY TSENG
#

from PokerManager import *

manager = PokerManager()

while True:
    click = manager.window.getMouse()
    manager.dealButton.onTarget(click)
    manager.quitButton.onTarget(click)

    if manager.balance == 0:
        manager.window.close()
        manager = PokerManager()
