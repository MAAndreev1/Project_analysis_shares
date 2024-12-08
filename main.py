import data_download as dd
import data_plotting as dplt


def main():
    """
        Основная функция, управляющая процессом загрузки, обработки данных и их визуализации.
        Запрашивает у пользователя ввод данных, вызывает функции загрузки и обработки данных,
        а затем передаёт результаты на визуализацию.
    """
    print("Добро пожаловать в инструмент получения и построения графиков биржевых данных.")
    print("Вот несколько примеров AAPLбиржевых тикеров, которые вы можете рассмотреть: AAPL (Apple Inc),"
          " GOOGL (Alphabet Inc), MSFT (Microsoft Corporation), AMZN (Amazon.com Inc), TSLA (Tesla Inc).")
    print("Общие периоды времени для данных о запасах включают: "
          "1д, 5д, 1мес, 3мес, 6мес, 1г, 2г, 5г, 10л, с начала года, макс.")

    ticker = input("Введите тикер акции (например, «AAPL» для Apple Inc): ")
    period = input("Введите период для данных (например, '1mo' для одного месяца): ")
    while True:
        threshold = input("Введите процент допустимых колебаний закрытия (целое число, например '5' для 'пяти %'): ")
        if  threshold.isdigit():
            threshold = float(threshold)
            break
        else:
            print("Введено неверное значение!")
    # ticker = "AAPL"
    # period = "1mo"
    # threshold = 5

    # Fetch stock data
    stock_data = dd.fetch_stock_data(ticker, period)

    # Add moving average to the data
    stock_data = dd.add_moving_average(stock_data)

    # Plot the data
    dplt.create_and_save_plot(stock_data, ticker, period)

    # Calculate average price of Close
    dd.calculate_and_display_average_price(stock_data)

    # Severe fluctuation notifications
    dd.notify_if_strong_fluctuations(stock_data, threshold)

    # Export to CSV
    dplt.export_data_to_csv(stock_data, "out")


if __name__ == "__main__":
    main()
