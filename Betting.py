
def bet(balance, bet_value):
    if bet_value > balance:
        return -1
    else:
        return balance - bet_value

