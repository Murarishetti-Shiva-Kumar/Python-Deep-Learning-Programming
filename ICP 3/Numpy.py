"""
Numpy
Using NumPy create random vector of size 20 having only float in the range 1-20.
Then reshape the array to 4 by 5
Then replace the max in each row by 0 (axis=1)
"""
import pandas as pd
import numpy as np

random_vector = np.linspace(1, 20, 20)  # creating array of size 20 having only float in the range 1-20.
print(random_vector)

random_vector = random_vector.reshape(4,5)  # reshape the array to 4 by 5
print("Numpy array after  reshaping to 4 by 5 looks like:")
print(random_vector)

print("replacing the max in each row by 0")
# replace the max in each row by 0
# np.where returns element depending on condition
random_vector = np.where(random_vector == np.amax(random_vector, axis=1).reshape(-1,1), 0, random_vector)

print(random_vector)