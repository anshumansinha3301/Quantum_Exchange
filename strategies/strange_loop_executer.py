import numpy as np

class StrangeLoopExecutor:
    def __init__(self, loop_depth=4):
        self.loop_depth = loop_depth

    def loop_execute(self, signal):
        trades = []
        phase = np.angle(np.fft.fft(signal))
        phase_loops = np.convolve(phase, np.hanning(self.loop_depth), mode='valid')
        trigger = np.gradient(phase_loops)
        for i in range(len(trigger)):
            if trigger[i] > 0.1:
                trades.append((i, 1))
            elif trigger[i] < -0.1:
                trades.append((i, -1))
        return trades
