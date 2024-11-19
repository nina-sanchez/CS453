import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define the size of the 3D grid
grid_size = 10

# Create a 3D array with gaps to form a lattice
# Keep only every other voxel "True" to create gaps
grid = np.zeros((grid_size, grid_size, grid_size), dtype=bool)
grid[::2, ::2, ::2] = True  # Keep every second voxel along each axis

# Plot the 3D lattice of cubes
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection='3d')

# Create the voxel visualization
ax.voxels(grid, facecolors="blue", edgecolor="k", alpha=0.9)

# Set labels and title
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")
ax.set_zlabel("Z-axis")
ax.set_title("3D Lattice of Cubes")

# Show the visualization
plt.show()

