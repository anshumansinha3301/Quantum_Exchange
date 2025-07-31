# Quantum Chaos Exchange

Quantum Chaos Exchange is an algorithmic trading system that uses techniques from chaos theory, entropy-based modeling, and neural network architectures to analyze time-series data and generate data-driven trading signals.

This project was developed as part of the GitHub Global Hackathon 2025.

---

## 📌 Overview

This system explores the application of nonlinear dynamics, signal entropy, and mathematical modeling to construct strategies that respond to complex patterns in financial markets. It does not rely on traditional indicators but instead uses advanced signal processing and state-space projections.

---

## 📂 Components

### 1. Signal Processing
- **ChaoticStateTracker**: Extracts nonlinear signals from price series using combined oscillatory transformations.
- **EntropyWaveRouter**: Computes entropy gradients and curvature-based energy across the signal timeline.
- **SingularityBreachDetector**: Identifies potential breakpoints in signal velocity or volatility spikes.

### 2. Modeling
- **LorenzFieldEncoder**: Encodes time series data using Lorenz attractor equations to capture hidden dynamics.
- **QMapGenerator**: Generates structured high-dimensional mappings for latent feature extraction.
- **RegimeMemoryNetwork**: Tracks statistical memory of signal regimes to infer transitions.
- **AttractorLSTM**: A recurrent neural network designed to capture temporal patterns from chaotic states.

### 3. Strategy Layer
- **EntropicArbitrageEngine**: Executes position logic based on entropy-weighted decisions.
- **StrangeLoopExecutor**: Trades based on phase loops and feedback from signal frequency domain.
- **HypercycleExtractor**: Detects phase-aligned patterns and possible trade rotations.

---

## 🧪 Experiments

Example analysis notebooks can be found under the `experiments/` folder:
- `entropic_surface_analysis.py` — visualizes entropy waves over time
- `attractor_pathways.py` — plots encoded trajectories using Lorenz system dynamics

---

## ⚙️ Configuration

All engine settings and model parameters can be adjusted in:

```yaml
# config/engine_config.yaml

engine:
  signal_length: 2048
  entropy_threshold: 0.15
  execution_window: 128
  alpha_scale: 1.2
  lorenz:
    sigma: 10.0
    rho: 28.0
    beta: 2.6667
  regime_model:
    decay: 0.92
  attractor_lstm:
    input_size: 1
    hidden_size: 64
    num_layers: 2
  routes:
    enable_entropy_wave: true
    enable_breach_detection: true

