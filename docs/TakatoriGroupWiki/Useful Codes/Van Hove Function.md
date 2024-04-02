

Got this from Chat GPT: Need to check the normalization. No guarantee it's correct. 
```python
import numpy as np
import matplotlib.pyplot as plt

# Load your 3D trajectory data (assuming it's in a format like XYZ coordinates)
# For example, let's say you have an array called 'coordinates' with shape (num_frames, num_particles, 3)

# Define parameters
num_frames, num_particles, _ = coordinates.shape
max_distance = 10.0  # Maximum distance to consider
num_bins = 100  # Number of bins for distance histogram
lag_time = 1  # Lag time in frames

# Initialize an array to store the Van Hove function
van_hove = np.zeros(num_bins)

# Initialize an array to store the count of pairs in each bin
pair_counts = np.zeros(num_bins)

# Calculate the pair distances with lag time and populate pair_counts
for i in range(num_frames - lag_time):
    for j in range(num_particles):
        for k in range(num_particles):
            if j != k:
                distance = np.linalg.norm(coordinates[i, j] - coordinates[i + lag_time, k])
                if distance < max_distance:
                    bin_index = int((distance / max_distance) * num_bins)
                    van_hove[bin_index] += 1
                    pair_counts[bin_index] += 1

# Normalize the Van Hove function
dr = max_distance / num_bins
van_hove /= (pair_counts * 4 * np.pi * dr**2 * np.arange(1, num_bins+1))

# Plot the Van Hove function
distances = np.linspace(0, max_distance, num_bins)
plt.plot(distances, van_hove)
plt.xlabel('Distance (Å)')
plt.ylabel('Van Hove Function')
plt.show()


```