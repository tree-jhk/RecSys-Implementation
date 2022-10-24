import numpy as np

# cos_sim = (두 벡터의 내적) / (두 벡터의 크기의 곱)
def cos_sim(a:np.array, b:np.array):
    inner_product = np.dot(a, b)
    size_of_a = np.linalg.norm(a)
    size_of_b = np.linalg.norm(b)
    return inner_product / (size_of_a * size_of_b)