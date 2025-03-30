import numpy as np
import xarray as xr
import matplotlib.pyplot as plt

# Load NetCDF file
file_path = r"C:\Users\usame\Downloads\glm-3.1.1\Mendota\output\output.nc"
ds = xr.open_dataset(file_path)

# Check variable names
print("Dataset Variables:", ds.variables)

# Extract temperature, depth, and time
temperature = ds['temp']  # Temperature array (time, depth)
depths = ds['z']  # Depth levels (time, depth)
time = ds['time']  # Time variable

# Compute average temperature at each depth (averaged over time)
avg_temp_at_depth = temperature.mean(dim='time').values.squeeze()  # (500,)

# Select the first time step for depth (to match dimensions)
depths_fixed = depths[0, :].values.squeeze()  # (500,)

# 🔍 Print some sample values
print("\nSample Depth Values:", depths_fixed[:10])
print("Sample Temp Values:", avg_temp_at_depth[:10])

# 🔄 Ensure depth is in correct order
if np.any(np.diff(depths_fixed) < 0):
    print("\n⚠ Depth is decreasing! Sorting it correctly.")
    sorted_indices = np.argsort(depths_fixed)
    depths_fixed = depths_fixed[sorted_indices]
    avg_temp_at_depth = avg_temp_at_depth[sorted_indices]

# 📊 Plot depth vs temperature
plt.figure(figsize=(8, 6))
plt.plot(avg_temp_at_depth, depths_fixed, color='r', marker='o', linestyle='-')

plt.gca().invert_yaxis()  # Depth increases downward
plt.xlabel("Temperature (°C)")
plt.ylabel("Depth (m)")
plt.title("Average Water Temperature at Each Depth")
plt.grid()
plt.show()
