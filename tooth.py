import numpy as np
import matplotlib.pyplot as plt
from skimage import measure  # For isosurface extraction

# Load the volume
filename = r"C:\Users\ktkim\Downloads\tooth_103x94x161_uint8.raw"
shape = (161, 94, 103)  # Depth, Height, Width
dtype = np.uint8

volume = np.fromfile(filename, dtype=dtype).reshape(shape)

# Step 1: Choose an isovalue
isovalue = 100 # Adjust this value to isolate the tooth structure

# Step 2: Extract the isosurface
verts, faces, _, _ = measure.marching_cubes(volume, level=isovalue)

# Step 3: Plot the isosurface
fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, projection='3d')

# Create a surface plot using the extracted vertices and faces
ax.plot_trisurf(
    verts[:, 0], verts[:, 1], verts[:, 2], triangles=faces, cmap='gray', edgecolor='none'
)

ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')
plt.title(f"3D Isosurface Visualization (Isovalue={isovalue})")
plt.show()
