import numpy as np

class QMapGenerator:
    def __init__(self, dimension):
        self.dimension = dimension

    def generate_qmap(self, seed):
        np.random.seed(seed)
        base = np.random.randn(self.dimension, self.dimension)
        q = np.dot(base, base.T)
        eigvals, eigvecs = np.linalg.eigh(q)
        q_normalized = eigvecs @ np.diag(np.tanh(eigvals)) @ eigvecs.T
        chaotic_map = np.sin(q_normalized ** 2 + np.pi / 7) * np.exp(-q_normalized)
        return chaotic_map
