import pandas as pd
import numpy as np

class TickStreamLoader:
    def __init__(self, path):
        self.path = path

    def load_ticks(self):
        df = pd.read_csv(self.path)
        time = pd.to_datetime(df['timestamp'])
        price = df['price'].astype(float)
        micro_movements = np.diff(price, prepend=price[0])
        normalized = (micro_movements - micro_movements.mean()) / micro_movements.std()
        return normalized
