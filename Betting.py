def bet(balance, bet_value):
    if bet_value > balance:
        return -1
    else:
        return balance - bet_value


def calculateWinnings(bet_value, hand_value, high_card):  # calculates the multiplier
    # type: (int, int, int) -> int

    # straight flush (8), straight (4)
    if hand_value == 8 or hand_value == 4:
        if high_card == 14:
            return 250 * bet_value
        return 50 * bet_value

    # 4 of a kind
    if hand_value == 7:
        return 25 * bet_value

    # full house
    if hand_value == 6:
        return 9 * bet_value

    # flush
    if hand_value == 5:
        return 6 * bet_value

    # 3 of a kind
    if hand_value == 3:
        return 3 * bet_value

    # 2 pair
    if hand_value == 2:
        return 2 * bet_value

    # pair or jacks or better
    if hand_value == 1:
        if high_card >= 11:
            return bet_value

    # nothing
    return 0
