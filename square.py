import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import OpenVisus as ov  # Assuming you have this library for loading the dataset

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

# Function to create a voxel-based structure from your dataset
def create_voxel_from_data(dataset, grid_size):
    # Assuming the dataset is a 3D grid of scalar values that can be thresholded for voxel inclusion
    # You may need to adjust this to suit the exact format of your dataset
    x = np.linspace(0, dataset.shape[0]-1, grid_size)
    y = np.linspace(0, dataset.shape[1]-1, grid_size)
    z = np.linspace(0, dataset.shape[2]-1, grid_size)
    
    X, Y, Z = np.meshgrid(x, y, z)
    
    # Create a boolean mask to determine which voxels to plot based on dataset values
    # This condition can be modified depending on the dataset's actual values
    voxel_condition = dataset > 0  # Example: select voxels where the dataset value is greater than 0
    
    return X, Y, Z, voxel_condition

# Visualization function to plot the voxel data
def plot_voxel_structure(X, Y, Z, voxel_condition, box_size=1, height=1):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    
    # Plot each long box inside the voxel grid
    for i in range(len(X)):
        for j in range(len(Y)):
            for k in range(len(Z)):
                if voxel_condition[i, j, k]:
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

# Dynamically load the dataset from the website
dataset_url = 'https://klacansky.com/open-scivis-datasets/nucleon/nucleon.idx'
cache_dir = '.'  # Directory to store cached data
dataset = ov.load_dataset(dataset_url, cache_dir=cache_dir)

# Define the region of interest (adjust as needed)
data = dataset.read(x=(0, 41), y=(0, 41), z=(0, 41))

# Adjust the grid size depending on the resolution you want
grid_size = 10  # Resolution of the voxel grid

# Create the voxel structure from the dataset
X, Y, Z, voxel_condition = create_voxel_from_data(data, grid_size)

# Plot the voxel structure
plot_voxel_structure(X, Y, Z, voxel_condition, box_size=0.5, height=5)
