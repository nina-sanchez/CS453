import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection



# Function to create a long box (rectangular prism) at a given position
def create_long_box(x, y, z, size=1, height=1):
    # Define the 8 corners of a long box (rectangular prism)
    box = [
        # Bottom face
        [[x, y, z], [x + size, y, z], [x + size, y + size, z], [x, y + size, z]],
        # Top face
        [[x, y, z + height], [x + size, y, z + height], [x + size, y + size, z + height], [x, y + size, z + height]],
        # Front face
        [[x, y, z], [x + size, y, z], [x + size, y, z + height], [x, y, z + height]],
        # Back face
        [[x, y + size, z], [x + size, y + size, z], [x + size, y + size, z + height], [x, y + size, z + height]],
        # Left face
        [[x, y, z], [x, y + size, z], [x, y + size, z + height], [x, y, z + height]],
        # Right face
        [[x + size, y, z], [x + size, y + size, z], [x + size, y + size, z + height], [x + size, y, z + height]]
    ]
    return box

# Function to create a voxel-based hemisphere with long boxes
def create_voxel_hemisphere(radius, grid_size, box_size=1):
    x = np.linspace(-radius, radius, grid_size)
    y = np.linspace(-radius, radius, grid_size)
    z = np.linspace(0, radius, grid_size)
    
    X, Y, Z = np.meshgrid(x, y, z)
    
    # Equation for the hemisphere (x^2 + y^2 + z^2 <= r^2 and z >= 0)
    hemisphere_voxels = (X**2 + Y**2 + Z**2 <= radius**2) & (Z >= 0)
    
    return X, Y, Z, hemisphere_voxels

# Visualization
def plot_voxel_hemisphere(X, Y, Z, hemisphere_voxels, box_size=1, height=1):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    
    # Plot each long box inside the hemisphere
    for i in range(len(X)):
        for j in range(len(Y)):
            for k in range(len(Z)):
                if hemisphere_voxels[i, j, k]:
                    x_voxel = X[i, j, k]
                    y_voxel = Y[i, j, k]
                    z_voxel = Z[i, j, k]
                    
                    # Create a long box (rectangular prism) at this position
                    box = create_long_box(x_voxel, y_voxel, z_voxel, size=box_size, height=height)
                    
                    # Plot the box (rectangular prism)
                    ax.add_collection3d(Poly3DCollection(box, facecolors='black', linewidths=1, edgecolors='w', alpha=0.9))

    # Set the aspect ratio to be equal and the axes labels
    ax.set_box_aspect([1, 1, 1])
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    
    plt.show()

# Parameters
radius = 5  # Radius of the hemisphere
grid_size = 10  # Resolution of the grid (higher means more detailed, lower means larger voxels)
box_size = 0.5  # The width of each long box (voxel)
height = 5  # The height of each long box (spanning vertically)

# Create and plot the voxel hemisphere with long boxes
X, Y, Z, hemisphere_voxels = create_voxel_hemisphere(radius, grid_size, box_size)
plot_voxel_hemisphere(X, Y, Z, hemisphere_voxels, box_size, height)

