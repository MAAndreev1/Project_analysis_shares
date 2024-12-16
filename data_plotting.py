import matplotlib.pyplot as plt
import pandas as pd


def create_and_save_plot(data, ticker, period, style, filename=None):
    """
        Создаёт график, отображающий цены закрытия и скользящие средние.
        Предоставляет возможность сохранения графика в файл.
        Параметр filename опционален; если он не указан, имя файла генерируется автоматически.
    """
    plt.figure(figsize=(10, 6))
    if style != '':
        plt.style.use(style=style)

    if 'Date' not in data:
        if pd.api.types.is_datetime64_any_dtype(data.index):
            dates = data.index.to_numpy()
            plt.plot(dates, data['Close'].values, label='Close Price')
            plt.plot(dates, data['Moving_Average'].values, label='Moving Average')
            plt.plot(dates, data['RSI'].values, label='RSI')
            plt.plot(dates, data['std'].values, label='std')
        else:
            print("Информация о дате отсутствует или не имеет распознаваемого формата.")
            return
    else:
        if not pd.api.types.is_datetime64_any_dtype(data['Date']):
            data['Date'] = pd.to_datetime(data['Date'])
        plt.plot(data['Date'], data['Close'], label='Close Price')
        plt.plot(data['Date'], data['Moving_Average'], label='Moving Average')
        plt.plot(data['Date'], data['RSI'], label='RSI')
        plt.plot(data['Date'], data['std'], label='std')

    plt.title(f"{ticker} Цена акций с течением времени")
    plt.xlabel("Дата")
    plt.ylabel("Цена")
    plt.legend()

    if filename is None:
        filename = f"{ticker}_{period}_stock_price_chart.png"

    plt.savefig(filename)
    print(f"График сохранен как {filename}")


def export_data_to_csv(data, filename):
    """
        Принимать DataFrame и наименование для будущего файла.
        Создает файл расширения ".csv" из DataFrame.
    """
    data.to_csv(f"{filename}.csv")
    print(f"Данные по выгрузке сохранены в {filename}.csv")
