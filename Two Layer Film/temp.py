import numpy as np
import matplotlib.pyplot as plt


def calculate_reflectance_double_layer(n1, n2, wavelength, thickness_ratio):
    n_s = 1.52  # Refractive index of the substrate
    n_0 = 1  # Refractive index of the incident medium
    delta_1 = np.pi / 2  # Quarter-wave optical thickness for both layers

    # Reflection coefficients for the first and second layers
    r1 = (n_0 - n1) / (n_0 + n1)
    r2 = (n1 - n2) / (n1 + n2)

    # Reflectance formula for a double-layer thin film
    R = np.abs((r1 + r2) / (1 + r1 * r2)) ** 2

    return R * 100  # Convert reflectance to percentage


# Parameters for the three cases
wavelengths = np.linspace(400, 700, 100) * 1e-9  # Wavelength range from 400nm to 700nm
thickness_ratio_a = 1 / 4
thickness_ratio_b = 1 / 2
thickness_ratio_c = 1 / 2

n1_a, n2_a = 1.65, 2.1
n1_b, n2_b = 1.38, 1.6
n1_c, n2_c = 1.38, 1.85

# Calculate reflectance for each case
reflectance_values_a = calculate_reflectance_double_layer(
    n1_a, n2_a, wavelengths, thickness_ratio_a
)
reflectance_values_b = calculate_reflectance_double_layer(
    n1_b, n2_b, wavelengths, thickness_ratio_b
)
reflectance_values_c = calculate_reflectance_double_layer(
    n1_c, n2_c, wavelengths, thickness_ratio_c
)

# Plotting the results
plt.plot(wavelengths * 1e9, reflectance_values_a, label="Case (a)")
plt.plot(wavelengths * 1e9, reflectance_values_b, label="Case (b)")
plt.plot(wavelengths * 1e9, reflectance_values_c, label="Case (c)")

# Finalizing the plot
plt.title("Reflectance from a Double-Layer Film vs Wavelength")
plt.xlabel("Wavelength (nm)")
plt.ylabel("Reflectance (%)")
plt.legend()
plt.grid(False)
plt.show()
