import numpy as np
from sentence_transformers import SentenceTransformer

# ==========================================
# 1. SIMILARITY FUNCTIONS FROM SCRATCH
# ==========================================

def dot_product_scratch(v1, v2):
    # Dono vectors ke elements ko multiply karke sum karna
    return sum(x * y for x, y in zip(v1, v2))

def magnitude_scratch(v):
    # Vector ki length nikalna: sqrt(x1^2 + x2^2 + ...)
    return sum(x ** 2 for x in v) ** 0.5

def cosine_similarity_scratch(v1, v2):
    dot_prod = dot_product_scratch(v1, v2)
    mag1 = magnitude_scratch(v1)
    mag2 = magnitude_scratch(v2)
    
    if mag1 == 0 or mag2 == 0:
        return 0.0
    
    # Formula: (A . B) / (||A|| * ||B||)
    return dot_prod / (mag1 * mag2)


# ==========================================
# 2. EXPERIMENT WITH ALL-MINILM-L6-V2
# ==========================================

print("HuggingFace Model load ho raha hai...")
model = SentenceTransformer("all-MiniLM-L6-v2")
print("Model Ready! 🚀\n")

# Sample documents jinka comparison karna hai
docs = [
    "I love building autonomous AI agents with Python.",      # Doc 0
    "Developing voice AI receptionists is very exciting.",    # Doc 1
    "Today the weather is cloudy and it might rain heavily."  # Doc 2
]

# Text ko embeddings (vectors) me badlein
embeddings = model.encode(docs)

print(f"Doc 0 vector shape: {embeddings[0].shape} (384 Dimensions)")
print(f"Doc 1 vector shape: {embeddings[1].shape}")
print(f"Doc 2 vector shape: {embeddings[2].shape}\n")


# ==========================================
# 3. TESTING SIMILARITY
# ==========================================

# Compare Doc 0 and Doc 1 (Tech vs Tech)
sim_0_1 = cosine_similarity_scratch(embeddings[0], embeddings[1])

# Compare Doc 0 and Doc 2 (Tech vs Weather)
sim_0_2 = cosine_similarity_scratch(embeddings[0], embeddings[2])

print("--- RESULTS FROM SCRATCH FUNCTION ---")
print(f"Similarity (AI Agents vs Voice AI): {sim_0_1 * 100:.2f}%")
print(f"Similarity (AI Agents vs Weather) : {sim_0_2 * 100:.2f}%")