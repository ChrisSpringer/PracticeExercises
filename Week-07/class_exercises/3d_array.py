# Christopher Springer
# 11/23/2026

import numpy as np

# Create a 3D array with Numpy
sales = np.array([
    [[100, 200, 300],
     [400, 500, 600]],

     [[700,800,900],
      [1000,1100,1200]]
])

# Display the 3D array
print('3D Numpy Array: ')
print(sales)

# Display the shape of the array
print('\nArray Shape: ', sales.shape)

# Display the number of dimensions
print('Number of Dimensions: ', sales.ndim)

# Access an element in the array
print('\nElement at position [0,1,2]: ', sales[0,1,2])