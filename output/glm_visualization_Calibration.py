import xarray as xr
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

# Load the NetCDF file
file_path = r"C:\Users\usame\Downloads\glm-3.1.1\Mendota\output\output.nc"
ds = xr.open_dataset(file_path)

# Extract temperature and time
temperature = ds['temp']  # (time, depth)
time = ds['time'].values  # Convert xarray time to numpy array

# Compute mean temperature over depth
simulated_temp = temperature.mean(dim='z').values  # Shape (2920,)

# Ensure correct shape: Flatten if necessary
simulated_temp = simulated_temp.flatten()

# Generate synthetic data with correct broadcasting
synthetic_temp = simulated_temp.copy()
sin_term = 2 * np.sin(2 * np.pi * np.arange(len(time)) / len(time))
synthetic_temp += sin_term

# Debug: Print shapes to verify
print("Shape of simulated_temp:", simulated_temp.shape)  # (2920,)
print("Shape of synthetic_temp:", synthetic_temp.shape)  # (2920,)

# Compute error metrics
rmse = np.sqrt(mean_squared_error(synthetic_temp, simulated_temp))
mae = mean_absolute_error(synthetic_temp, simulated_temp)
r2 = r2_score(synthetic_temp, simulated_temp)

# Print results
print(f"RMSE: {rmse:.2f} °C")
print(f"MAE: {mae:.2f} °C")
print(f"R²: {r2:.2f}")

# Plot results
plt.figure(figsize=(12, 5))
plt.plot(time, simulated_temp, label="Simulated", color='b')
plt.plot(time, synthetic_temp, label="Synthetic", linestyle="dashed", color='r')
plt.xlabel("Time")
plt.ylabel("Temperature (°C)")
plt.title("GLM-Simulated vs. Synthetic Temperature")
plt.legend()
plt.grid()
plt.show()
