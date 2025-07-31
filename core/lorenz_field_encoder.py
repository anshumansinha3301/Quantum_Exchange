import numpy as np

class LorenzFieldEncoder:
    def __init__(self, sigma=10.0, rho=28.0, beta=8.0/3.0):
        self.sigma = sigma
        self.rho = rho
        self.beta = beta

    def encode(self, initial_state, dt, steps):
        x, y, z = initial_state
        result = np.zeros((steps, 3))
        for i in range(steps):
            dx = self.sigma * (y - x)
            dy = x * (self.rho - z) - y
            dz = x * y - self.beta * z
            x += dx * dt
            y += dy * dt
            z += dz * dt
            result[i] = [x, y, z]
        return result
