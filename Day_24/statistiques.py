stats_array = np.array([[1, 2, 3], [4, 55, 44], [7, 8, 9]])

print("Min:", stats_array.min())
print("Max:", stats_array.max())
print("Mean:", stats_array.mean())
print("Median:", np.median(stats_array))
print("Standard deviation:", stats_array.std())

print("Min par colonne:", np.amin(stats_array, axis=0))
print("Max par ligne:", np.amax(stats_array, axis=1))
