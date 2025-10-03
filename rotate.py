def left_rotate(arr, d):
    n = len(arr)
    # Ensure d is within the bounds of array length
    d = d % n 
    return arr[d:] + arr[:d]

# Example usage:
my_array = [1, 2, 3, 4, 5, 6, 7]
rotations = 2
rotated_array = left_rotate(my_array, rotations)
print(f"Original array: {my_array}")
print(f"Left rotated array by {rotations}: {rotated_array}") 
