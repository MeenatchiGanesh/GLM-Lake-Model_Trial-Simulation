import xarray as xr
import numpy as np
import matplotlib.pyplot as plt

# Load the NetCDF file
file_path = r"C:\Users\usame\Downloads\glm-3.1.1\Mendota\output\output.nc"
ds = xr.open_dataset(file_path)


print(ds)


temperature = ds['temp']  # Temperature variable
depths = ds['z']  # Depth levels
time = ds['time']  # Time

# Compute average lake temperature over depth
avg_temp = temperature.mean(dim='z')

# Compute average temperature at each depth over time
avg_temp_depth = temperature.mean(dim='time')

# Plot average lake temperature over time
plt.figure(figsize=(12, 5))
plt.plot(time, avg_temp.squeeze(), label="Avg Temp", color='b')
plt.xlabel("Time")
plt.ylabel("Temperature (°C)")
plt.title("Average Water Temperature Over Time")
plt.legend()
plt.grid()
plt.show()

# Plot temperature variations with depth
plt.figure(figsize=(8, 6))
for i in range(0, len(time), len(time) // 4):  # Seasonal snapshots
    plt.plot(avg_temp_depth[:, i], depths, label=str(np.datetime_as_string(time[i], unit='D')))

plt.gca().invert_yaxis()  # Depth increases downward
plt.xlabel("Temperature (°C)")
plt.ylabel("Depth (m)")
plt.title("Seasonal Temperature Profiles")
plt.legend()
plt.grid()
plt.show()
