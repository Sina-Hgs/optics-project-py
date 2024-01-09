import numpy as np
import matplotlib.pyplot as plt


def reflectance_double_layer(wavelength, n0, ns, n1, n2, d1, d2):
    """
    Calculate reflectance for a double-layer film at a range of wavelengths using mathematical formula.

    Parameters:
    - wavelengths: Array of wavelengths in nm
    - n0: Refractive index of incident medium
    - ns: Refractive index of substrate
    - n1: Refractive index of layer 1
    - n2: Refractive index of layer 2
    - d1: Thickness of layer 1 in nm
    - d2: Thickness of layer 2 in nm

    Returns:
    - Reflectance values for each wavelength
    """

    r01 = (n0 - n1) / (n0 + n1)
    r12 = (n1 - n2) / (n1 + n2)
    r2s = (n2 - ns) / (n2 + ns)

    phi_1 = 2 * np.pi * n1 * d1 / wavelength
    phi_2 = 2 * np.pi * n2 * d2 / wavelength

    reflectance_amplitude = (
        (r01 + r12 * np.exp(1j * phi_1))
        / (1 + r12 * r2s * np.exp(2j * phi_1))
        * np.exp(1j * phi_2)
    )

    R = np.abs(reflectance_amplitude) ** 2

    return R * 100


# Wavelength range
wavelengths_range = np.linspace(300e-9, 800e9, 1000)
fixed_wavelength = 550e9

# Parameters for case (a)
n0_a = 1
ns_a = 1.52
n1_a = 1.65
n2_a = 2.1
d1_a = fixed_wavelength / 4
d2_a = fixed_wavelength / 4

# Parameters for case (b)
n0_b = 1
ns_b = 1.52
n1_b = 1.38
n2_b = 1.6
d1_b = fixed_wavelength / 4
d2_b = fixed_wavelength / 2

# Parameters for case (c)
n0_c = 1
ns_c = 1.52
n1_c = 1.38
n2_c = 1.85
d1_c = fixed_wavelength / 4
d2_c = fixed_wavelength / 2

# Calculate reflectance for each case
reflectance_a = reflectance_double_layer(
    wavelengths_range, n0_a, ns_a, n1_a, n2_a, d1_a, d2_a
)
reflectance_b = reflectance_double_layer(
    wavelengths_range, n0_b, ns_b, n1_b, n2_b, d1_b, d2_b
)
reflectance_c = reflectance_double_layer(
    wavelengths_range, n0_c, ns_c, n1_c, n2_c, d1_c, d2_c
)

# Plotting
plt.figure(figsize=(10, 6))

# Plot for Case (a)
plt.plot(wavelengths_range, reflectance_a, label="Case (a)")

# Plot for Case (b)
plt.plot(wavelengths_range, reflectance_b, label="Case (b)")

# Plot for Case (c)
plt.plot(wavelengths_range, reflectance_c, label="Case (c)")

plt.xlabel("Wavelength (nm)")
plt.ylabel("Reflectance")
plt.title("Reflectance of Double-Layer Film vs Wavelength")
plt.legend()
plt.show()
