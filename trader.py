from market import Market
from strategy import generate_signal
from risk import position_size
from portfolio import Portfolio

market = Market()
portfolio = Portfolio()

prices = []

def run_trade():
    data = market.tick()
    price = data["BTC"]

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

    portfolio_value = portfolio.total_value(price)

    # 🔥 STOP LOGIC
    if portfolio.is_finished(price):
        portfolio.history.append("🏁 STOP raggiunto")
        return price, "STOP", amount, portfolio_value

    return price, signal, amount, portfolio_value
