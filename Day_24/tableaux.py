array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

print(array[0:2, 0:2])

print(array[::-1, ::-1])

reshaped = array.reshape(3, 3)
flattened = reshaped.flatten()
