from strategies.entropic_arbitrage import EntropicArbitrageEngine
from core.chaotic_state_tracker import ChaoticStateTracker
from core.singularity_breach_detector import SingularityBreachDetector
from core.entropy_wave_router import EntropyWaveRouter
from core.qmap_generator import QMapGenerator
from core.lorenz_field_encoder import LorenzFieldEncoder
import numpy as np

def run():
    tracker = ChaoticStateTracker()
    signal = tracker.track_signal(2048)
    detector = SingularityBreachDetector(threshold=1.9)
    breaches = detector.detect(signal)
    router = EntropyWaveRouter()
    entropy_routed = router.route_entropy_packet(signal)
    qmap = QMapGenerator(dimension=5).generate_qmap(seed=1337)
    encoded = LorenzFieldEncoder().encode(initial_state=(1.0, 1.0, 1.0), dt=0.005, steps=1500)
    engine = EntropicArbitrageEngine()
    trades = engine.execute(entropy_routed)
    print(f"Executed {len(trades)} entropic trades from chaotic attractor states.")

if __name__ == "__main__":
    run()
