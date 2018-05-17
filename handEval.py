# COPYRIGHT 2018 BY LARRY TSENG
# Evaluates the value of a given hand of cards

ranks = ['2', '3', '4', '5', '6', '7', '8', '9', 't', 'j', 'q', 'k', 'a']
suits = ['s', 'h', 'd', 'c']


def sortExtractHand(hand):
    # type: (list) -> tuple[list, list]
    """
    Helper function: Sorts and extracts a list of cards according to ranks
    :param hand: a list of cards (sorted)
    :return: two separate lists of ranks and suits
    """
    hand.sort(key=lambda item: ranks.index(item[0]))  # sorts the hand according to rank

    # split the ranks and suits
    extracted_ranks = []
    extracted_suits = []

    for card in hand:
        extracted_ranks.append(card[0])
        extracted_suits.append(card[1])

    return extracted_ranks, extracted_suits


def checkIfSame(cards):
    # type: (list) -> bool
    """
    Helper function: Determines if adjacent ranks are the same (thus all ranks are the same)
    :param cards: a list of ranks (sorted)
    :return: whether or not the ranks are the same or not
    """
    for index in range(len(cards) - 1):  # 0...len(cards) - 1
        if cards[index] != cards[index + 1]:
            return False

    return True


def checkIfRanksConsecutive(cards):
    # type: (list) -> bool
    """
    Helper function: Determines if adjacent ranks are consecutive (in order)
    :param cards: a list of ranks (sorted)
    :return: whether or not the ranks are consecutive or not
    """
    for index in range(len(cards) - 1):  # 0...len(cards) - 1
        if ranks.index(cards[index]) + 1 != ranks.index(cards[index + 1]):
            if not (cards[index] == '5' and cards[index + 1] == 'a'):  # checks if ace is next to 5
                return False

    return True


def checkForPairs(cards):
    # type: (list) -> int
    """
    Helper function: Determines the number of pairs of cards in a hand (according to rank)
    :param cards: a list of ranks (sorted)
    :return: the number of pairs
    """
    count = 0
    for index in range(len(cards) - 1):
        if checkIfSame(cards[index:index + 2]):  # grabs two cards
            count += 1

    return count


def handType(hand):
    """
    Determines the maximum value of the hand
    :param hand: a list of cards (unsorted/sorted)
    :return: the value of the hand
    """
    # type: list -> int

    extracted_ranks, extracted_suits = sortExtractHand(hand)

    # Straight Flush (suit is the same, rank is consecutive)
    if checkIfRanksConsecutive(extracted_ranks) and checkIfSame(extracted_suits):
        return 8

    # 4 of a kind
    if checkIfSame(extracted_ranks[0:4]) or checkIfSame(extracted_ranks[1:5]):
        return 7

    # Full House (first three ranks are same, second two ranks are same) (or the opposite)
    if (checkIfSame(extracted_ranks[0:3]) and checkIfSame(extracted_ranks[3:5]) or
            checkIfSame(extracted_ranks[0:2]) and checkIfSame(extracted_ranks[2:5])):
        return 6

    # Flush
    if checkIfSame(extracted_suits):
        return 5

    # Straight
    if checkIfRanksConsecutive(extracted_ranks):
        return 4

    # 3 of a kind
    if checkIfSame(extracted_ranks[0:3]) or checkIfSame(extracted_ranks[1:4]) or checkIfSame(extracted_ranks[2:5]):
        return 3

    # 2 pair
    if checkForPairs(extracted_ranks) == 2:
        return 2

    # Pair
    if checkForPairs(extracted_ranks):
        return 1

    # High Card
    return 0  # return 0 for high card


def highCard(hand):
    # type: (list) -> int
    """
    Determines the value of the highest tie-breaking card
    :param hand: a list of cards (unsorted/sorted)
    :return: the value of the highest card
    """
    hand_type = handType(hand)

    extracted_ranks, extracted_suits = sortExtractHand(hand)

    # if straight flush or straight
    if hand_type == 8 or hand_type == 4:
        if extracted_ranks[-1] == 'a' and extracted_ranks[-2] == '5':
            return 5
        else:
            return ranks.index(extracted_ranks[-1][0]) + 2

    # four of a kind (return a card in the middle of the deck [the fourth card] in the deck)
    if hand_type == 7:
        return ranks.index(extracted_ranks[3]) + 2

    # full house (find the groups of 3)
    if hand_type == 6:
        if checkIfSame(extracted_ranks[0:3]):
            return ranks.index(extracted_ranks[0]) + 2
        else:
            return ranks.index(extracted_ranks[4]) + 2

    # flush
    if hand_type == 5:
        return ranks.index(extracted_ranks[-1]) + 2     # returns the value of the last rank

    # 3 of a kind
    if hand_type == 3:
        if checkIfSame(extracted_ranks[0:3]):
            return ranks.index(extracted_ranks[0]) + 2
        elif checkIfSame(extracted_ranks[1:4]):
            return ranks.index(extracted_ranks[1]) + 2
        elif checkIfSame(extracted_ranks[2:5]):
            return ranks.index(extracted_ranks[2]) + 2

    # 2 pair
    if hand_type == 2:
        highest_pair = '2'
        for index in range(len(extracted_ranks) - 1):
            if checkIfSame(extracted_ranks[index:index + 2]):
                if ranks.index(extracted_ranks[index]) > ranks.index(highest_pair):
                    highest_pair = extracted_ranks[index]

        return ranks.index(highest_pair) + 2

    # pair
    if hand_type == 1:
        for index in range(len(extracted_ranks) - 1):
            if checkIfSame(extracted_ranks[index:index + 2]):
                return ranks.index(extracted_ranks[index]) + 2

    # high card
    if hand_type == 0:
        return ranks.index(extracted_ranks[-1][0]) + 2

    return 0


# TEST CASES
# print handType(['ts', 'ks', 'qs', 'as', 'js']),  # 'should be 8'
# print handType(['as', 'ac', '4s', 'ad', 'ah']),  # 'should be 7'
# print handType(['as', 'ac', '4s', 'ad', '4c']),  # 'should be 6'
# print handType(['2s', '4s', '5s', 'ks', '3s']),  # 'should be 5'
# print handType(['2s', '4s', '5s', 'ac', '3s']),  # 'should be 4'
# print handType(['3s', 'ac', '4s', '4d', '4h']),  # 'should be 3'
# print handType(['as', 'ac', '4s', '4d', 'kh']),  # 'should be 2'
# print handType(['as', '2s', '4s', '6s', '2c']),  # 'should be 1'
# print handType(['7s', '5c', '4s', '3s', '2s']),  # 'should be 0'
#
# print highCard(['ts', 'ks', 'qs', 'as', 'js']),  # 'should be 14'
# print highCard(['as', 'ac', '4s', 'ad', 'ah']),  # 'should be 14'
# print highCard(['as', 'ac', '4s', 'ad', '4c']),  # 'should be 14'
# print highCard(['2s', '4s', '5s', 'ks', '3s']),  # 'should be 13'
# print highCard(['2s', '4s', '5s', 'ac', '3s']),  # 'should be 5'
# print highCard(['3s', 'ac', '4s', '4d', '4h']),  # 'should be 4'
# print highCard(['as', 'ac', '4s', '4d', 'kh']),  # 'should be 14'
# print highCard(['as', '2s', '4s', '6s', '2c']),  # 'should be 2'
# print highCard(['7s', '5c', '4s', '3s', '2s']),  # 'should be 7'
# print highCard(['as', '2c', '3s', '4s', '5s']),  # 'should be 5'
