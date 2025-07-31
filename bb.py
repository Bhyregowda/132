import matplotlib.pyplot as plt
import numpy as np

x = np.array([6])
y = np.array([2])
plt.plot(x, y, 'o')  # 'o' specifies a circular marker
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Single Point Plot")
plt.grid(True)
plt.show()
