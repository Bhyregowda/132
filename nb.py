import matplotlib.pyplot as plt
import numpy as np

# Define single coordinate points
x1, y1 = 0, 0
x2, y2 = 6, 25

# Plot the line between the two points
plt.plot([x1, x2], [y1, y2])  # Still needs lists to connect the points

# Plot the individual points
plt.plot(x1, y1, 'o')  # First point
plt.plot(x2, y2, 'o')  # Second point

plt.show()
