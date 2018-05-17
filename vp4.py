# COPYRIGHT 2018 BY LARRY TSENG
# A script to spawn PokerManagers and manage clicks

from PokerManager import *

manager = PokerManager()

while True:

    # check for clicks
    click = manager.window.getMouse()
    manager.dealButton.onTarget(click)
    manager.quitButton.onTarget(click)

    if manager.balance == 0:
        manager.window.close()
        manager = PokerManager()    # assigns manager to a new PokerManager()
