import numpy as np

class HypercycleExtractor:
    def __init__(self):
        self.shift = 37

    def extract(self, signal):
        embedded = np.lib.stride_tricks.sliding_window_view(signal, self.shift)
        matrix = embedded @ embedded.T
        u, s, vh = np.linalg.svd(matrix)
        modes = np.sum(np.abs(s) > 1e-2)
        scores = np.sin(np.linspace(0, np.pi, modes)) * s[:modes]
        direction = np.sign(np.gradient(scores))
        trades = [(i, int(d)) for i, d in enumerate(direction) if d != 0]
        return trades
