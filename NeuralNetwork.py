# Rudimentary neural network to predict XOR gate

import numpy as np

# Input Data: 4x2 array to predict xor, first taking std. inputs
inputs = np.array([
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
])

# Expected Output Data: What we expect the neural network to output, 4x1
outputs = np.array([
    [0],
    [1],
    [1],
    [0]
])


input_size = 2
hidden_size = 2
output_size = 1

#Weights and biases initialization (random initialization seed)
np.random.seed(0) #for reproducibility
weights_input_hidden = np.random.rand(input_size, hidden_size)
weights_hidden_output = np.random.rand(hidden_size, output_size)
biases_hidden = np.random.rand(1, hidden_size)
biases_output = np.random.rand(1, output_size)