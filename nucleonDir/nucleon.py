import OpenVisus as ov
import numpy as np
from mayavi import mlab

# Dynamically load the dataset from the website per the provided import code
dataset_url = 'https://klacansky.com/open-scivis-datasets/nucleon/nucleon.idx'
cache_dir = '.' 
dataset = ov.load_dataset(dataset_url, cache_dir=cache_dir)

# Define the region of interest based on website's parameters
data = dataset.read(x=(0, 41), y=(0, 41), z=(0, 41))

# Convert data to a NumPy array and set the volume
volume = np.array(data, dtype=np.uint8)

# Set isovalue to recommended one from website to isolate nucelon 
isovalue = 124.5

# Visualize the isosurface using Mayavi
mlab.figure(size=(800, 800), bgcolor=(1, 1, 1))

# Add title to visualization
mlab.title(f"Nucleon Visualization", color=(0, 0, 0), size=0.5)

# Define the slicing plane and create a cut along the Z-axis
cut_position = 20

# Create the two parts of the volume (split along the z-axis)
volume_before_cut = volume[:, :, :cut_position]  # First part before the cut
volume_after_cut = volume[:, :, cut_position:]  # Second part after the cut

# Add a gap by adding empty space between them
gap_size = 40

# Create a new array with a larger size to accommodate the gap and the second part
volume_after_cut_shifted = np.zeros((volume_after_cut.shape[0], volume_after_cut.shape[1], volume_after_cut.shape[2] + gap_size), dtype=np.uint8)

# Shift the data in the second part, leaving a gap along the Z-axis
volume_after_cut_shifted[:, :, gap_size:] = volume_after_cut

# Visualize the first part (before the cut)
mlab.contour3d(volume_before_cut, contours=[isovalue], opacity=1.0, colormap='gray')

# Visualize the second part (after the cut) with the gap
mlab.contour3d(volume_after_cut_shifted, contours=[isovalue], opacity=1.0, colormap='gray')

# Show the visualization
mlab.show()
