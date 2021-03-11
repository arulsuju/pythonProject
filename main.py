import matplotlib.pyplot as plt
import numpy as np

xs = np.linspace(0, 9, 100)
ys = np.sin(xs)
plt.plot(xs, ys, label="First application")
plt.legend()
