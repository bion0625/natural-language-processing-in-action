from itertools import permutations

result = [" ".join(combo) for combo in permutations("Good morning Rosa".split(), 3)]

print(result)

s = """Find textbooks with titles containing NLP or 'natural' and 'language', or 'computational' and 'linguistics'."""
result = len(set(s.split()))
print(result)

import numpy as np
result = np.arange(1, 12 + 1).prod()
print(result)