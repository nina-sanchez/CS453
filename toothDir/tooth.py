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
mlab.contour3d(volume, contours=[isovalue], opacity=0.5, colormap='gray')

# Add axes and title for better context
mlab.axes(xlabel='X-axis', ylabel='Y-axis', zlabel='Z-axis')
mlab.title(f"3D Isosurface Visualization (Isovalue={isovalue})")

# Show the visualization
mlab.show()
