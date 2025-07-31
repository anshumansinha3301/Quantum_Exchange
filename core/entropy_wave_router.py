import numpy as np
from scipy.signal import hilbert

class EntropyWaveRouter:
    def __init__(self):
        pass

    def route_entropy_packet(self, signal):
        analytic = hilbert(signal)
        envelope = np.abs(analytic)
        log_env = np.log1p(envelope)
        entropy = -log_env * np.gradient(log_env)
        curvature = np.gradient(np.gradient(signal))
        route = entropy + 0.3 * curvature
        norm_route = np.tanh(route / (np.std(route) + 1e-6))
        return norm_route
