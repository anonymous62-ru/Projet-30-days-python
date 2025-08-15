import matplotlib.pyplot as plt
import seaborn as sns

sns.set()
plt.hist(normal_array, color="gray", bins=50)
plt.title("Distribution normale")
plt.show()
