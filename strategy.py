import numpy as np

def generate_signal(prices):
    if len(prices) < 5:
        return "HOLD"

    short_ma = np.mean(prices[-3:])
    long_ma = np.mean(prices[-5:])

    if short_ma > long_ma:
        return "BUY"

    if short_ma < long_ma:
        return "SELL"

    return "HOLD"
