import yfinance as yf


def fetch_stock_data(ticker, period='1mo'):
    stock = yf.Ticker(ticker)
    data = stock.history(period=period)
    return data


def add_moving_average(data, window_size=5):
    data['Moving_Average'] = data['Close'].rolling(window=window_size).mean()
    return data


def calculate_and_display_average_price(data):
    all_price = [i for i in data['Close']]
    average_price = sum(all_price) / len(all_price)
    print('Средняя цена закрытия акций за заданный период равне,',average_price)
