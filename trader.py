from market import Market
from strategy import generate_signal
from risk import position_size
from portfolio import Portfolio

market = Market()
portfolio = Portfolio()

prices = []

def run_trade():
    price = market.tick()

    prices.append(price)

    signal = generate_signal(prices)

    amount = position_size(
        portfolio.balance,
        price
    )

    if signal == "BUY":
        portfolio.buy(price, amount)

    elif signal == "SELL":
        portfolio.sell(price, amount)

    portfolio_value = portfolio.value(price)

    return (
        price,
        signal,
        amount,
        portfolio_value
    )
