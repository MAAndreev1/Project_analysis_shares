import pandas as pd
import plotly.express as px


def create_plotly(data):
    """
        Создаёт интерактивный график, отображающий цены закрытия и скользящие средние.
    """
    if 'Date' not in data:
        if pd.api.types.is_datetime64_any_dtype(data.index):
            dates = data.index.to_numpy()
            fig = px.line(data, x=dates, y=["Close", "Moving_Average", "RSI", "std"])
            fig.show()
        else:
            print("Информация о дате отсутствует или не имеет распознаваемого формата.")
            return
    else:
        if not pd.api.types.is_datetime64_any_dtype(data['Date']):
            fig = px.line(data, x=["Date"], y=["Close", "Moving_Average", "RSI", "std"])
            fig.show()
