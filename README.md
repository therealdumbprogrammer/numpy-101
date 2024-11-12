# 📊 NumPy Cheat Sheet

## 🔍 Introduction
**NumPy** (Numerical Python) is a fundamental library for numerical computing in Python. It provides support for large, multi-dimensional arrays and matrices, along with a collection of mathematical functions to operate on these arrays efficiently.

## 🛠️ Installation

```bash
pip install numpy
```

Or, if using Anaconda:

```bash
conda install numpy
```

## 📦 Importing NumPy

```python
import numpy as np
```

## 📐 Creating Arrays

### From Lists

```python
# 1D Array
arr1 = np.array([1, 2, 3, 4, 5])

# 2D Array
arr2 = np.array([[1, 2, 3], [4, 5, 6]])
```

### Using Built-in Functions

```python
# Zeros
zeros = np.zeros((3, 4))  # 3x4 array of zeros

# Ones
ones = np.ones((2, 3))     # 2x3 array of ones

# Arange
arange = np.arange(0, 10, 2)  # [0, 2, 4, 6, 8]

# Linspace
linspace = np.linspace(0, 1, 5)  # [0. , 0.25, 0.5 , 0.75, 1. ]
```

## 🔑 Array Attributes

```python
print(arr1.shape)  # Shape of the array
print(arr1.dtype)  # Data type of elements
print(arr1.size)   # Total number of elements
```

## ➕➖✖️➗ Array Operations

### Arithmetic Operations

```python
# Addition
sum_arr = arr1 + 5  # Adds 5 to each element

# Subtraction
diff_arr = arr1 - 2  # Subtracts 2 from each element

# Element-wise Multiplication
prod_arr = arr1 * 3  # Multiplies each element by 3

# Element-wise Division
div_arr = arr1 / 2  # Divides each element by 2
```

### Universal Functions (ufuncs)

```python
# Square Root
sqrt_arr = np.sqrt(arr1)

# Exponential
exp_arr = np.exp(arr1)

# Natural Logarithm
log_arr = np.log(arr1)
```

## 🎯 Indexing and Slicing

### 1D Arrays

```python
first_element = arr1[0]         # First element
sliced_arr = arr1[1:4]          # Elements from index 1 to 3
```

### 2D Arrays

```python
element = arr2[0, 2]            # Element at row 0, column 2
first_column = arr2[:, 0]       # All rows, first column
```

## 🔄 Array Manipulation

### Reshaping

```python
reshaped_arr = arr2.reshape((3, 2))  # Reshape to 3x2 array
```

### Stacking

```python
# Vertical Stacking
vstack_arr = np.vstack((arr1, arr3))

# Horizontal Stacking
hstack_arr = np.hstack((arr1, arr3))
```

### Splitting

```python
split_arr = np.split(arr3, 5)  # Split arr3 into 5 sub-arrays
```

## 📈 Broadcasting

**Broadcasting** allows NumPy to perform arithmetic operations on arrays of different shapes.

```python
broadcast_sum = arr1 + 5  # Adds 5 to each element of arr1
```

## 🎲 Random Number Generation

```python
# Random Floats in [0, 1)
random_floats = np.random.rand(3, 2)

# Random Integers between 0 and 9
random_ints = np.random.randint(0, 10, size=(3, 2))

# Random Normal Distribution
random_norm = np.random.randn(2, 3)  # Mean=0, Std=1
```

## 📊 Common Functions

```python
# Sum of all elements
total_sum = np.sum(arr1)

# Mean of elements
mean_val = np.mean(arr1)

# Minimum and Maximum
min_val = np.min(arr1)
max_val = np.max(arr1)

# Standard Deviation
std_dev = np.std(arr1)
```

## 🧩 Advanced Operations

### Masking and Boolean Indexing

```python
# Create a boolean mask
mask = arr1 > 3

# Apply mask to array
filtered_arr = arr1[mask]
```

### Fancy Indexing

```python
# Select specific indices
indices = [0, 2, 4]
selected_elements = arr1[indices]
```

### Conditional Operations

```python
# Replace elements based on condition
arr1[arr1 < 3] = 0
```

## 📝 Best Practices

- **Use Vectorized Operations:** Leverage NumPy's optimized functions instead of Python loops for better performance.
- **Avoid Unnecessary Copies:** Use views where possible to save memory.
- **Understand Broadcasting Rules:** Familiarize yourself with how NumPy broadcasts arrays to avoid unexpected results.
- **Use Appropriate Data Types:** Choose the right `dtype` to optimize memory usage and performance.
