# COPYRIGHT 2018 BY LARRY TSENG
#

ranks = ['2', '3', '4', '5', '6', '7', '8', '9', 't', 'j', 'q', 'k', 'a']
suits = ['s', 'h', 'd', 'c']


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
    straight_flush = True

    for index in range(len(extracted_ranks) - 1):   # 0...4
        if ranks.index(extracted_ranks[index]) + 1 != ranks.index(extracted_ranks[index + 1]):
            # however if its a...5, it is still a straight flush?
            straight_flush = False

        if suits.index(extracted_suits[index]) != suits.index(extracted_suits[index + 1]):
            straight_flush = False

    if straight_flush:
        return 8

    # 4 of a kind
    four_of_a_kind = True

    # check 1st four
    for index in range(0, 3):
        pass

    for index in range(1, 4):
        pass


    # check 2nd four

    return hand  # for debug


def highCard(hand):
    # type: (list) -> int

    pass


# TEST CASES
print handType(['ts', 'ks', 'qs', 'as', 'js']),  # 'should be 8'
print handType(['as', 'ac', '4s', 'ad', 'ah']),  # 'should be 7'
print handType(['as', 'ac', '4s', 'ad', '4c']),  # 'should be 6'
print handType(['2s', '4s', '5s', 'ks', '3s']),  # 'should be 5'
print handType(['2s', '4s', '5s', 'ac', '3s']),  # 'should be 4'
print handType(['3s', 'ac', '4s', '4d', '4h']),  # 'should be 3'
print handType(['as', 'ac', '4s', '4d', 'kh']),  # 'should be 2'
print handType(['as', '2s', '4s', '6s', '2c']),  # 'should be 1'
print handType(['7s', '5c', '4s', '3s', '2s']),  # 'should be 0'

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
