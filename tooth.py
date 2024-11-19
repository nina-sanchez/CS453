import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Load the volume
filename = r"C:\Users\ktkim\Downloads\tooth_103x94x161_uint8.raw"
shape = (161, 94, 103)  # Depth, Height, Width
dtype = np.uint8

volume = np.fromfile(filename, dtype=dtype).reshape(shape)

# Create a 3D isosurface plot
z, y, x = volume.nonzero()  # Nonzero points in the volume

fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, projection='3d')
ax.scatter(x, y, z, c=volume[z, y, x], cmap='twilight', marker='o', s=0.1)

ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')
plt.title("3D Visualization")
plt.show()