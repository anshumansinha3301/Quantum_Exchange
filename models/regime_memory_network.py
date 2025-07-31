import numpy as np

class RegimeMemoryNetwork:
    def __init__(self, decay=0.92):
        self.memory = np.zeros(3)
        self.decay = decay

    def forward(self, input_signal):
        features = np.array([
            np.mean(input_signal),
            np.std(input_signal),
            np.median(np.abs(input_signal - np.mean(input_signal)))
        ])
        self.memory = self.decay * self.memory + (1 - self.decay) * features
        logits = np.tanh(np.dot(self.memory, np.array([0.8, -0.6, 1.2])))
        state = int(logits > 0)
        return state
