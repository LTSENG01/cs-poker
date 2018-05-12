# COPYRIGHT 2018 BY LARRY TSENG
#

ranks = ['2', '3', '4', '5', '6', '7', '8', '9', 't', 'j', 'q', 'k', 'a']
suits = ['s', 'h', 'd', 'c']


def checkIfSame(cards):
    # type: (list) -> bool
    for index in range(len(cards) - 1):  # 0...len(cards) - 1
        if cards[index] != cards[index + 1]:
            return False

    return True


def checkIfRanksConsecutive(cards):
    # type: (list) -> bool
    for index in range(len(cards) - 1):  # 0...len(cards) - 1
        if ranks.index(cards[index]) + 1 != ranks.index(cards[index + 1]):
            if not (cards[index] == '5' and cards[index + 1] == 'a'):   # checks if ace is next to 5
                return False

    return True


def checkForPairs(cards):
    # type: (list) -> int
    count = 0
    for index in range(len(cards) - 1):
        if checkIfSame(cards[index:index + 2]):  # grabs two cards
            count += 1

    return count


def handType(hand):
    # type: (list) -> int

    hand.sort(key=lambda item: ranks.index(item[0]))  # sorts the hand according to rank

    # split the ranks and suits
    extracted_ranks = []
    extracted_suits = []

    for card in hand:
        extracted_ranks.append(card[0])
        extracted_suits.append(card[1])

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

    pass


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
print highCard(['ts', 'ks', 'qs', 'as', 'js']),  # 'should be 14'
print highCard(['as', 'ac', '4s', 'ad', 'ah']),  # 'should be 14'
print highCard(['as', 'ac', '4s', 'ad', '4c']),  # 'should be 14'
print highCard(['2s', '4s', '5s', 'ks', '3s']),  # 'should be 13'
print highCard(['2s', '4s', '5s', 'ac', '3s']),  # 'should be 5'
print highCard(['3s', 'ac', '4s', '4d', '4h']),  # 'should be 4'
print highCard(['as', 'ac', '4s', '4d', 'kh']),  # 'should be 14'
print highCard(['as', '2s', '4s', '6s', '2c']),  # 'should be 2'
print highCard(['7s', '5c', '4s', '3s', '2s']),  # 'should be 7'
print highCard(['as', '2c', '3s', '4s', '5s']),  # 'should be 5'
