import numpy as np

class SingularityBreachDetector:
    def __init__(self, threshold):
        self.threshold = threshold

    def detect(self, signal):
        diff = np.diff(signal)
        spikes = np.abs(diff) > self.threshold
        shifts = np.sign(diff[1:] - diff[:-1])
        inflections = (shifts[1:] != shifts[:-1]).astype(int)
        events = np.where(spikes[1:-1] * inflections > 0)[0] + 1
        return events
