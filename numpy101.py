import numpy as np

one_dim = np.array([1, 2, 3])

print("1D Array-----")
print(one_dim)
print(one_dim.shape)
print(one_dim.size)
print(one_dim.dtype)

two_dim = np.array([[2, 4, 6], [3, 5, 7]])

print("2D Array-----")
print(two_dim)
print(two_dim.shape)
print(two_dim.size)
print(two_dim.dtype)

print("Adding 1D and 2D Arrays--------")
print(one_dim + two_dim)
print("Subtracting 1D and 2D Arrays--------")
print(one_dim - two_dim)
print("Multiplying 1D and 2D Arrays--------")
print(one_dim * two_dim)
print("Dividing 1D and 2D Arrays--------")
print(one_dim / two_dim)

print("Square root of 1D")
print(np.sqrt(one_dim))

print("Square of 2D")
print(np.square(two_dim))

print("Indexing and Slicing--------")
print("1D Array---")
print(one_dim[1])
print(one_dim[0:])

print("2D Array---")
print(two_dim[0])
print(two_dim[1])
print(two_dim[0, 1])
print(two_dim[:, 1])

print("Reshaping-----")
print(two_dim)
print(two_dim.reshape(3, 2))

print("Broadcasting---")
print(two_dim + 10)

print("Stacking-----")
one_dim_1 = np.array([4, 5, 6])
print("Vertical stack---")
print(np.vstack((one_dim, one_dim_1)))
print("Horizontal stack---")
print(np.hstack((one_dim, one_dim_1)))

