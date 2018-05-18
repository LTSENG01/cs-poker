# COPYRIGHT 2018 BY LARRY TSENG
# Calculates the bets


def bet(balance, bet_value):
    # type: (int, int) -> int
    """
    Checks if the bet is valid, if so, return the new balance
    :param balance: current balance
    :param bet_value: value of the bet
    :return: balance or -1 if invalid
    """
    if bet_value > balance:
        return -1
    else:
        return balance - bet_value


def calculateWinnings(bet_value, hand_value, high_card):  # calculates the multiplier
    # type: (int, int, int) -> int
    """
    Calculates the winnings based on the hand and the bet
    :param bet_value: the value of the bet
    :param hand_value: the value of the hand
    :param high_card: the value of the tie-breaking card
    :return: the value of the winnings
    """
    # straight flush (8), straight (4)
    if hand_value == 8 or hand_value == 4:
        if high_card == 14:
            return (250 * bet_value) + bet_value
        return (50 * bet_value) + bet_value

    # 4 of a kind
    if hand_value == 7:
        return (25 * bet_value) + bet_value

    # full house
    if hand_value == 6:
        return (9 * bet_value) + bet_value

    # flush
    if hand_value == 5:
        return (6 * bet_value) + bet_value

    # 3 of a kind
    if hand_value == 3:
        return (3 * bet_value) + bet_value

    # 2 pair
    if hand_value == 2:
        return (2 * bet_value) + bet_value

    # pair or jacks or better
    if hand_value == 1:
        if high_card >= 11:
            return 2 * bet_value

    # nothing
    return 0
