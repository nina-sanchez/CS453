import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from skimage import measure
from skimage.filters import gaussian  # Correct module for Gaussian smoothing

# Create a synthetic volumetric dataset or load your own
shape = (30, 30, 30)
volume = np.zeros(shape, dtype=np.uint8)

# Add some cubic structures to the volume
volume[10:20, 10:20, 10:20] = 1  # Cube 1
volume[15:25, 15:25, 5:15] = 1  # Cube 2

# Visualization Function for Voxels
def plot_voxel_grid(ax, volume):
    ax.voxels(volume, edgecolor="k", facecolors="white", alpha=0.9)
    ax.set_box_aspect([1, 1, 1])  # Uniform scaling

# Visualization Function for Smoothed Surface
def plot_smoothed_surface(ax, volume, level=0.5):
    verts, faces, _, _ = measure.marching_cubes(volume, level=level)
    mesh = Poly3DCollection(verts[faces], alpha=0.7, edgecolor="k")
    ax.add_collection3d(mesh)
    ax.set_box_aspect([1, 1, 1])
    ax.set_xlim(0, volume.shape[0])
    ax.set_ylim(0, volume.shape[1])
    ax.set_zlim(0, volume.shape[2])

# Plot the grids
fig = plt.figure(figsize=(12, 12))

# Top-left: Initial voxel grid
ax1 = fig.add_subplot(221, projection="3d")
plot_voxel_grid(ax1, volume)
ax1.set_title("Voxel Grid - Original")

# Top-right: Voxel grid with modified data
volume[8:12, 8:12, 8:12] = 1  # Modify volume
ax2 = fig.add_subplot(222, projection="3d")
plot_voxel_grid(ax2, volume)
ax2.set_title("Voxel Grid - Modified")

# Bottom-left: Smoothed surface representation
ax3 = fig.add_subplot(223, projection="3d")
plot_smoothed_surface(ax3, volume)
ax3.set_title("Smoothed Surface - Initial")

# Bottom-right: Modified smoothed surface with Gaussian smoothing
smoothed_volume = gaussian(volume, sigma=1)  # Apply Gaussian smoothing
ax4 = fig.add_subplot(224, projection="3d")
plot_smoothed_surface(ax4, smoothed_volume)
ax4.set_title("Smoothed Surface - Gaussian")

plt.tight_layout()
plt.show()
