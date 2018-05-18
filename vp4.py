# COPYRIGHT 2018 BY LARRY TSENG
# A script to spawn PokerManagers and manage clicks

from PokerManager import *

manager = PokerManager()

while True:

    # check for clicks
    if manager.window.isOpen():
        click = manager.window.getMouse()
    else:
        manager.window.close()
        break

    if manager.dealButton.onTarget(click) and manager.balance == 0:     # if removed, it will continue to line 23
        continue

    if manager.quitButton.onTarget(click):
        break

    if manager.balance == 0 and manager.playAgainButton.onTarget(click):
        manager.window.close()
        manager = PokerManager()    # assigns manager to a new PokerManager()
