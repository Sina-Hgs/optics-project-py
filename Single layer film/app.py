import numpy as np
import matplotlib.pyplot as plt


# Function to calculate reflectance for thin film interference
def calculate_reflectance(ns, n1, delta):
    numerator = (
        n1**2 * (1 - ns) ** 2 * np.cos(delta) ** 2
        + (1 * ns - n1**2) ** 2 * np.sin(delta) ** 2
    )
    denominator = (
        n1**2 * (1 + ns) ** 2 * np.cos(delta) ** 2
        + (1 * ns + n1**2) ** 2 * np.sin(delta) ** 2
    )
    return numerator / denominator * 100  # Convert reflectance to percent


# Parameters
n_s = 1.52  # Refractive index of the substrate (glass)
n_1_values = [1.2, 1.4, 1.6, 1.8, 2.0]  # Different refractive indices of the thin film
wavelength = 500e-9  # Wavelength of light in meters (e.g., 500 nm)
delta_ratio_range = np.linspace(
    -1e-10, 1e10, 400
)  # Optical path difference ratio range

# Plotting for different film indices
for n_1 in n_1_values:
    delta_values = delta_ratio_range * wavelength
    reflectance_values = [
        calculate_reflectance(n_s, n_1, delta) for delta in delta_values
    ]
    plt.plot(delta_ratio_range, reflectance_values, label=f"n_1={n_1}")

# Finalizing the plot
plt.axhline(
    y=calculate_reflectance(n_s, n_s, wavelength / 2),
    color="gray",
    linestyle="dashed",
    label="Uncoated Glass",
)
plt.title("Reflectance vs Optical Path Difference Ratio")
plt.xlabel("Optical Path Difference Ratio (δ/λ)")
plt.ylabel("Reflectance (%)")
plt.legend()
plt.grid(False)
plt.show()
