import xarray as xr
import numpy as np
import matplotlib.pyplot as plt

# Load the NetCDF file
file_path = r"C:\Users\usame\Downloads\glm-3.1.1\Mendota\output\output.nc"
ds = xr.open_dataset(file_path)

# Extract temperature, depth, and time
temperature = ds['temp']  # Temperature variable
depths = ds['z']  # Depth levels
time = ds['time']  # Time variable

# 1. Calculate the overall average water temperature (over time and depth)
overall_avg_temp = temperature.mean().item()
print(f"Overall Average Lake Temperature: {overall_avg_temp:.2f} °C")

# 2. Calculate the average water temperature over depth (for each time step)
avg_temp_over_depth = temperature.mean(dim='z')

# 3. Calculate the average water temperature at each depth (averaged over time)
avg_temp_at_depth = temperature.mean(dim='time')

# Plot average water temperature over time (depth-averaged)
plt.figure(figsize=(12, 5))
plt.plot(time, avg_temp_over_depth.squeeze(), label="Avg Temp over Depth", color='b')
plt.xlabel("Time")
plt.ylabel("Temperature (°C)")
plt.title("Average Water Temperature Over Time (Depth-Averaged)")
plt.legend()
plt.grid()
plt.show()

# Plot temperature variations with depth (time-averaged)
plt.figure(figsize=(8, 6))
plt.plot(avg_temp_at_depth, depths, label="Avg Temp at Depth", color='r')

plt.gca().invert_yaxis()  # Depth increases downward
plt.xlabel("Temperature (°C)")
plt.ylabel("Depth (m)")
plt.title("Average Water Temperature at Each Depth (Time-Averaged)")
plt.legend()
plt.grid()
plt.show()
