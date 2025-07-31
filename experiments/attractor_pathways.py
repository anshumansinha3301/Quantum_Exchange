import matplotlib.pyplot as plt
from core.lorenz_field_encoder import LorenzFieldEncoder

encoder = LorenzFieldEncoder()
trajectory = encoder.encode(initial_state=(1.0, 1.0, 1.0), dt=0.005, steps=3000)

x, y, z = trajectory[:,0], trajectory[:,1], trajectory[:,2]

fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')
ax.plot(x, y, z, lw=0.5, color='darkred')
ax.set_title("Lorenz Attractor Pathway")
plt.show()
