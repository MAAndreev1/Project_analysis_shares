from dataclasses import dataclass

import yfinance as yf


def fetch_stock_data(ticker, period='1mo'):
    """
        Получает исторические данные об акциях для указанного тикера и временного периода.
        Возвращает DataFrame с данными.
        Допустимый <period>: 1d,5d,1mo,3mo,6mo,1y,2y,5y,10y,ytd,max
    """
    stock = yf.Ticker(ticker)
    data = stock.history(period=period)
    return data


def add_moving_average(data, window_size=5):
    """
        Добавляет в DataFrame колонку со скользящим средним, рассчитанным на основе цен закрытия.
    """
    data['Moving_Average'] = data['Close'].rolling(window=window_size).mean()
    return data


def calculate_and_display_average_price(data):
    """
        Принимать DataFrame.
        Вычисляет и выводит в консоль среднюю цену закрытия акций за период в DataFrame.
    """
    all_price = [i for i in data['Close']]
    if len(all_price) != 0:
        average_price = sum(all_price) / len(all_price)
        print(f'Средняя цена закрытия акций за заданный период равна, {average_price}')


def notify_if_strong_fluctuations(data, threshold):
    """
        Принимать DataFrame и threshold (процент допустимых отклонений).
        Функция вычисляет максимальное и минимальное значения цены закрытия и сравнивать разницу с заданным порогом.
        Если разница превышает порог, пользователь получает уведомление.
    """
    extreme_values = [i for i in data['Close'] if i == max(data['Close']) or i == min(data['Close'])]
    if len(extreme_values) != 0:
        fluctuation = (extreme_values[-1] - extreme_values[0]) / extreme_values[0] * 100
        if abs(fluctuation) > threshold:
            print(f'Уведомление, колебания акции в выбранный период превысили заданный порог в {threshold} %'
                  f' и составил {round(fluctuation, 2)} %')