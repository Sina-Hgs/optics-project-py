import numpy as np
import matplotlib.pyplot as plt

materials = [
    ["Cryolite", 1.32],
    ["MgF₂", 1.38],
    ["SiO₂", 1.46],
    ["SiO₃", 1.78],
    ["Al₂O₃", 1.60],
    ["CeF₃", 1.65],
    ["ThO₂", 1.80],
    ["Nd₂O₃", 2.0],
    ["ZrO₂", 2.1],
    ["CeO₂", 2.35],
    ["ZnS", 2.35],
    ["TiO₂", 2.4],
]


# Function to calculate reflectance for thin film interference
def single_layer_reflectance(ns, n1, delta):
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


wavelength = 550e-9  # Wavelength of light in meters (e.g., 550 nm)

delta_ratio_range = np.linspace(
    -1e-11, 1e11, 200
)  # Optical path difference ratio range

# Plotting for different film indices
j = 0
for i in materials:
    delta_values = delta_ratio_range * wavelength
    reflectance_values = [
        single_layer_reflectance(n_s, materials[j][1], delta) for delta in delta_values
    ]
    plt.plot(
        np.linspace(300, 800, 200),
        reflectance_values,
        label=f"{materials[j][0]}={materials[j][1]}",
    )
    j = j + 1

# Finalizing the plot
plt.axhline(
    y=single_layer_reflectance(n_s, n_s, wavelength / 4),
    color="gray",
    linestyle="dashed",
    label="Uncoated Glass",
)
plt.title("Single Layer Films")
plt.xlabel("Wavelength (nm)")
plt.ylabel("Reflectance (%)")
plt.legend()
plt.grid(True)
plt.show()
