import OpenVisus as ov
import numpy as np
from mayavi import mlab

# Dynamically load the dataset from the website
dataset_url = 'https://klacansky.com/open-scivis-datasets/tooth/tooth.idx'
cache_dir = '.'  # Directory to store cached data
dataset = ov.load_dataset(dataset_url, cache_dir=cache_dir)

# Define the region of interest (adjust as needed)
data = dataset.read(x=(0, 103), y=(0, 94), z=(0, 161))

# Convert data to a NumPy array and set the volume
volume = np.array(data, dtype=np.uint8)

# Choose an isovalue
isovalue = 132.75  # Adjust this value to isolate the tooth structure

# Visualize the isosurface using Mayavi
mlab.figure(size=(800, 800), bgcolor=(1, 1, 1))

# Add axes and title for better context
mlab.axes(xlabel='X-axis', ylabel='Y-axis', zlabel='Z-axis')
mlab.title(f"Tooth Visualization", color=(0, 0, 0), size=0.5)

# Define the slicing plane and create a vertical cut along the Y-axis
cut_position = 47  # Change this value to control the cut position along the Y-axis

# Create the two parts of the volume (split along the y-axis)
volume_before_cut = volume[:, :cut_position, :]  # First part before the cut
volume_after_cut = volume[:, cut_position:, :]  # Second part after the cut

# To visually separate the two parts, add a gap by adding empty space between them
gap_size = 100  # Define the gap between the two volumes

# Create a new array with a larger size to accommodate the gap and the second part
volume_after_cut_shifted = np.zeros((volume_after_cut.shape[0], volume_after_cut.shape[1] + gap_size, volume_after_cut.shape[2]), dtype=np.uint8)

# Shift the data in the second part, leaving a gap along the Y-axis
volume_after_cut_shifted[:, gap_size:, :] = volume_after_cut

# Visualize the first part (before the cut)
mlab.contour3d(volume_before_cut, contours=[isovalue], opacity=1.0, colormap='gray')

# Visualize the second part (after the cut) with the gap
mlab.contour3d(volume_after_cut_shifted, contours=[isovalue], opacity=1.0, colormap='gray')

# Show the visualization
mlab.show()
