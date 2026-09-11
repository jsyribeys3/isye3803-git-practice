import matplotlib.pyplot as plt
import numpy as np

# Create x values
x = np.linspace(-10, 10, 100)

# Calculate y values (f(x) = x^2)
y = x**2

# Create the plot
plt.figure(figsize=(10, 6))
plt.plot(x, y, linewidth=2, color='blue')
plt.title('Plot of f(x) = x²', fontsize=16, fontweight='bold')
plt.xlabel('x', fontsize=12)
plt.ylabel('f(x) = x²', fontsize=12)
plt.grid(True, alpha=0.3)

# Show the plot
plt.show()
