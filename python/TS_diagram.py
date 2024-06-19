import matplotlib.pyplot as plt

# Sample temperature and salinity data
temperature = [10, 12, 14, 16, 18, 20, 22, 24, 26, 28]
salinity = [35, 35.5, 36, 36.5, 37, 37.5, 38, 38.5, 39, 39.5]

# Plotting the TS diagram
plt.scatter(salinity, temperature, c='blue', marker='o')
plt.xlabel('Salinity')
plt.ylabel('Temperature (°C)')
plt.title('TS Diagram')
plt.grid(True)

# Display the plot
plt.show()