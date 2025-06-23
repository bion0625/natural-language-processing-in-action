import numpy as np

v1 = np.array([1, 2, 3])
v2 = np.array([2, 3, 4])

result = v1.dot(v2)
print(f"result: {result}")

result = (v1 * v2).sum()
print(f"result: {result}")

result = sum(x1 * x2 for x1, x2 in zip(v1, v2))
print(f"result: {result}")
