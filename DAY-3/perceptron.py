import numpy as np

# Inputs
inputs = np.array([1, 2, 3])

# Weights
weights = np.array([0.2, 0.8, -0.5])

# Bias
bias = 2

# Output
output = np.dot(inputs, weights) + bias

print("Neuron Output:", output)