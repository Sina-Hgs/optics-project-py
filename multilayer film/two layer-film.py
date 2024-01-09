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


# Function to calculate reflectance for two layer film
def two_layer_reflectance(n_s, n_1, n_2, thickness, wavelength, theta):
    # Convert angle from degrees to radians
    theta_rad = np.radians(theta)

    # Calculate optical path difference
    delta = 4 * np.pi * n_1 * thickness / wavelength * np.cos(theta_rad)

    # Calculate reflectance formula
    numerator = (n_s**2 - n_2**2 + 2 * n_1 * n_s) * np.cos(delta) + 2 * n_1 * (
        n_1 - n_2
    ) * np.sin(delta)
    denominator = (n_s**2 + n_2**2 + 2 * n_1 * n_s) * np.cos(delta) + 2 * n_1 * (
        n_1 - n_2
    ) * np.sin(delta)

    reflectance = np.abs(numerator / denominator) ** 2

    return reflectance * 100  # Convert reflectance to percentage


# Parameters
n_s = 1.52  # Refractive index of the substrate (glass)
thickness = (550e-9) / 4  # Wavelength which is used for thickness of material
theta = 0  # Angle of incidence in degrees
wavelength_range = np.linspace(350e-9, 850e-9, 100)

# Plotting for different film indices
for i in range(len(materials)):
    plt.figure()  # Create a new figure for each value of i
    for j in range(len(materials)):
        if i != j:  # Skip combinations with the same material
            reflectance_values = [
                two_layer_reflectance(
                    n_s,
                    materials[i][1],
                    materials[j][1],
                    thickness,
                    wavelength,
                    theta,
                )
                for wavelength in wavelength_range
            ]
            plt.plot(
                np.linspace(350, 850, len(reflectance_values)),
                reflectance_values,
                label=f"{materials[i][0]} & {materials[j][0]}={materials[i][1]} & {materials[j][1]}",
            )

    # Finalizing the plot
    plt.title(f"Two Layer Films - {materials[i][0]}")
    plt.xlabel("Wavelength (nm)")
    plt.ylabel("Reflectance (%)")
    plt.legend()
    plt.grid(True)

# Display all plots
plt.show()
