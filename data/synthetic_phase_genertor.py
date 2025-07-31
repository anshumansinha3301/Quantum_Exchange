import numpy as np

class SyntheticPhaseGenerator:
    def __init__(self, steps=1024):
        self.steps = steps

    def generate(self):
        t = np.linspace(0, 20 * np.pi, self.steps)
        base = np.sin(t * 0.5) + 0.5 * np.sin(t * 2.5)
        noise = 0.3 * np.random.randn(self.steps)
        chaotic = base + noise
        warped = np.sin(np.sqrt(np.abs(chaotic))) + np.cos(chaotic * 0.8)
        final = warped + 0.1 * np.random.randn(self.steps)
        return final
