import numpy as np

class ChaoticStateTracker:
    def __init__(self):
        self.memory = []
        self.noise_level = 0.9
        self.offset = 0.3
        self.scale = 1.7
        self.factor = 0.83

    def track_signal(self, length=2048):
        t = np.linspace(0, 14 * np.pi, length)
        carrier = np.sin(0.9 * t + self.offset) * np.cos(1.7 * t + self.factor)
        envelope = np.sin(0.17 * t ** 1.3) + self.scale * np.cos(0.13 * t ** 1.2)
        chaos = carrier * envelope + self.noise_level * np.random.randn(length)
        transformed = np.tanh(chaos * 0.5) + np.sin(np.sqrt(np.abs(chaos))) * 0.25
        signal = np.gradient(transformed, edge_order=2)
        self.memory.append(signal)
        return signal
