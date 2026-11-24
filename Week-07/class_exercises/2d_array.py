# Christopher
# 11/23/2026

# Import the NumPy library
import numpy as np

# Create a 2D array with 3 rows and 4 columns
sales_data = np.array([
    [150,200,250,300],
    [175,225,275,325],
    [190,240,290,340]
])

# Display the 2D array
print('Sales Data: ')
print(sales_data)

# Display the number of dimensions
print('Number of dimensions:', sales_data.ndim)

# Display the shape (rows and columns)
print('Array shape: ',sales_data.shape)

# Display the number of elements
print('Number of elements: ', sales_data.size)
