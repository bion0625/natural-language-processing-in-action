import re
sentence = """Thomas Jefferson began building Monticello at the age of 26."""
pattern = re.compile(r"([-\s.,;!?])+")
tokens = pattern.split(sentence)
tokens = [x for x in tokens if x and x not in '- \t\n.,;!?']

print(f"tokens: {tokens}")

from nltk.util import ngrams
result = list(ngrams(tokens, 2))
print(f"result: {result}")

result = list(ngrams(tokens, 3))
print(f"result: {result}")

two_grams = list(ngrams(tokens, 2))
result = [" ".join(x) for x in two_grams]
print(f"result: {result}")
