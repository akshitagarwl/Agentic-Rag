import matplotlib.pyplot as plt
import numpy as np
from sklearn.manifold import TSNE
from sentence_transformers import SentenceTransformer

# 1. Model load karein
model = SentenceTransformer("all-MiniLM-L6-v2")

# 2. Kuch sample documents - 3 alag categories ke
sample_docs = [
    # Category 1: AI & Tech
    "Machine learning and neural networks are cool.",
    "Building conversational AI agents with large language models.",
    "Python is the primary language for data science.",
    
    # Category 2: Food & Cooking
    "I love baking fresh chocolate chip cookies.",
    "Italian pasta recipes require good olive oil.",
    "Spicy Indian curries have amazing flavor profiles.",
    
    # Category 3: Sports
    "The football match ended in a dramatic penalty shootout.",
    "Cricket requires immense patience and skill in test format.",
    "LeBron James scored forty points in last night's basketball game."
]

# Labels create kar rahe hain graph me color dene ke liye
colors = ['blue', 'blue', 'blue', 'green', 'green', 'green', 'red', 'red', 'red']
categories = ['Tech', 'Tech', 'Tech', 'Food', 'Food', 'Food', 'Sports', 'Sports', 'Sports']

print("Text ko vectors me convert kiya ja raha hai...")
embeddings = model.encode(sample_docs)

# 3. t-SNE Algorithm lagana (384D ko 2D me badalna)
# perplexity ko kam rakh rahe hain kyunki hamara data bohot chhota hai
tsne = TSNE(n_components=2, perplexity=2, random_state=42)
embeddings_2d = tsne.fit_transform(embeddings)

# 4. Graph Plot karna
plt.figure(figsize=(10, 8))

for i, doc in enumerate(sample_docs):
    # 2D coordinates points nikalna
    x, y = embeddings_2d[i, 0], embeddings_2d[i, 1]
    plt.scatter(x, y, color=colors[i], s=100, label=categories[i] if categories[i] not in plt.gca().get_legend_handles_labels()[1] else "")
    plt.text(x + 0.1, y + 0.1, f"Doc {i}", fontsize=9)

plt.title("Embedding Visualization using t-SNE (Day 8)")
plt.xlabel("Dimension 1")
plt.ylabel("Dimension 2")
plt.legend()
plt.grid(True, linestyle='--', alpha=0.6)

print("Graph save ho raha hai as 'embeddings_plot.png'...")
plt.savefig("embeddings_plot.png")
print("Done! Apne root folder me 'embeddings_plot.png' file ko open karke dekhiye. 🎉")