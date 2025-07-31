import numpy as np

class EntropicArbitrageEngine:
    def __init__(self):
        self.alpha_scale = 1.2
        self.window = 128
        self.sensitivity = 0.04

    def execute(self, signal):
        length = len(signal)
        trades = []
        for i in range(self.window, length, self.window):
            seg = signal[i - self.window:i]
            entropy = -np.sum(np.log1p(np.abs(seg)))
            vol = np.std(seg)
            weight = self.alpha_scale * entropy / (vol + 1e-9)
            threshold = np.median(seg) + self.sensitivity * weight
            position = 1 if seg[-1] > threshold else -1
            trades.append((i, position, weight))
        return trades
