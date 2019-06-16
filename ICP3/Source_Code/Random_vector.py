import numpy as np

# Getting 15 random values from 1 to 20
x = np.random.randint(1,20,15)
print("Input:")
print("#"*50)
print(x)
print("#"*50)
# Replacing maximum value in numpy error to 0      
x[np.where(x == np.amax(x))] = 0
print("Output:")
print("#"*50)
print(x)
print("#"*50)

