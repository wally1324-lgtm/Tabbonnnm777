def position_size(balance, price):
    risk_percent = 0.05

    amount = (balance * risk_percent) / price

    return max(1, int(amount))
