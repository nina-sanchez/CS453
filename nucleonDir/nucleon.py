import OpenVisus as ov
import numpy as np
from mayavi import mlab

# Dynamically load the dataset from the website
dataset_url = 'https://klacansky.com/open-scivis-datasets/nucleon/nucleon.idx'
cache_dir = '.'  # Directory to store cached data
dataset = ov.load_dataset(dataset_url, cache_dir=cache_dir)

# Define the region of interest (adjust as needed)
data = dataset.read(x=(0, 41), y=(0, 41), z=(0, 41))

# Convert data to a NumPy array
volume = np.array(data, dtype=np.uint8)

# Define the region to be visualized based on the isovalue
isovalue = 124.5
mask = volume <= isovalue  # Create a mask for values <= 124.5

# Apply the mask to filter out points where values are greater than 124.5
filtered_volume = np.where(mask, volume, 0)  # Set all non-nucleon values to 0

# Visualize the cubic lattice with Mayavi (showing only the nucleon structure)
mlab.figure(size=(800, 800), bgcolor=(1, 1, 1))

# Display the filtered volume (nucleon structure) as a 3D volume
mlab.pipeline.volume(mlab.pipeline.scalar_field(filtered_volume))

# Show the visualization and allow user interaction
mlab.show()