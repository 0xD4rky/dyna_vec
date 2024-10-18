import numpy as np
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
from embeddings import *

embedding_np = embedding.cpu().numpy()

plt.figure(figsize=(15, 5))

plt.subplot(1, 3, 1)
plt.plot(embedding_np[:100])
plt.title("First 100 values of the embedding")
plt.xlabel("Index")
plt.ylabel("Value")

plt.subplot(1, 3, 2)
plt.hist(embedding_np, bins=50)
plt.title("Histogram of embedding values")
plt.xlabel("Value")
plt.ylabel("Frequency")

plt.subplot(1, 3, 3)
plt.boxplot(embedding_np)
plt.title("Box plot of embedding values")
plt.ylabel("Value")

plt.tight_layout()
plt.show()

print(f"Embedding mean: {np.mean(embedding_np):.4f}")
print(f"Embedding std: {np.std(embedding_np):.4f}")
print(f"Embedding min: {np.min(embedding_np):.4f}")
print(f"Embedding max: {np.max(embedding_np):.4f}")
print(f"Embedding median: {np.median(embedding_np):.4f}")