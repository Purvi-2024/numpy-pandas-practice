import numpy as np

# Creating Arrays

arr1 = np.array([10, 20, 30, 40, 50])

print("Array:", arr1)

print("Type:", type(arr1))

print("Dimensions:", arr1.ndim)

print("Shape:", arr1.shape)

print("Size:", arr1.size)

print("Datatype:", arr1.dtype)

# Student Marks Example

marks = np.array([78, 85, 92, 67, 88])

print("\nStudent Marks:", marks)

print("Total Marks:", np.sum(marks))

print("Average Marks:", np.mean(marks))

print("Highest Marks:", np.max(marks))

print("Lowest Marks:", np.min(marks))