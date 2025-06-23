sentence = """Thomas Jefferson began building Monticello at the age of 26."""
result = sentence.split()
print(f"result: {result}")

result = str.split(sentence)
print(f"result: {result}")


import numpy as np

token_sequence = str.split(sentence)
vocab = sorted(set(token_sequence))
result = ' '.join(vocab)
print(f"result: {result}")

num_tokens = len(token_sequence)
print(f"num_tokens: {num_tokens}")

vocab_size = len(vocab)
onehot_vectors = np.zeros((num_tokens, vocab_size), int)

for i, word in enumerate(token_sequence):
    onehot_vectors[i, vocab.index(word)] = 1

print(f"onehot_vectors: {onehot_vectors}")


import pandas as pd

df = pd.DataFrame(onehot_vectors, columns=vocab)
print(f"df: \n{df}")

df[df == 0] = ''
print(f"df: \n{df}")


num_rows = 3000 * 3500 * 15
print(f"num_rows: {num_rows}")

num_bytes = num_rows * 1000000
print(f"num_bytes: {num_bytes}")
print(f"num_bytes / 1e9: {num_bytes / 1e9}")
print(f"num_bytes / 1e9 / 1000: {num_bytes / 1e9 / 1000}")

sentence_bow = {}
for token in sentence.split():
    sentence_bow[token] = 1

result = sorted(sentence_bow.items())
print(f"result: {result}")


df = pd.DataFrame(
    pd.Series(dict([token, 1] for token in sentence.split())),
    columns=['sent']
).T

sentences = """Thomas Jefferson began building Monticello at the age of 26.\n"""
sentences += """Construction was done mostly by local masons and carpenters.\n"""
sentences += """He moved into the South Pavilion in 1770.\n"""
sentences += """Turning Monticello into a neoclassical masterpiece was Jefferson's obsession."""

corpus = {}
for i, sent in enumerate(sentences.split("\n")):
    corpus['sent{}'.format(i)] = dict((tok, 1) for tok in sent.split())

df = pd.DataFrame.from_records(corpus).fillna(0).astype(int)

print(f"df: \n{df}")