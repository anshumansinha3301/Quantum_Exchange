import numpy as np
import matplotlib.pyplot as plt
from core.chaotic_state_tracker import ChaoticStateTracker
from core.entropy_wave_router import EntropyWaveRouter

tracker = ChaoticStateTracker()
signal = tracker.track_signal(4096)

router = EntropyWaveRouter()
entropy = router.route_entropy_packet(signal)

plt.figure(figsize=(14, 5))
plt.plot(entropy, color="black", linewidth=0.8)
plt.title("Entropic Field Over Signal Time", fontsize=14)
plt.grid(True)
plt.show()
