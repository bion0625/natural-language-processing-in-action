import pandas as pd

sentences = """Thomas Jefferson began building Monticello at the age of 26.\n"""
sentences += """Construction was done mostly by local masons and carpenters.\n"""
sentences += """He moved into the South Pavilion in 1770.\n"""
sentences += """Turning Monticello into a neoclassical masterpiece was Jefferson's obsession."""

corpus = {}
for i, sent in enumerate(sentences.split("\n")):
    corpus['sent{}'.format(i)] = dict((tok, 1) for tok in sent.split())

df = pd.DataFrame.from_records(corpus).fillna(0).astype(int)

# df = df.T
result = df.sent0.dot(df.sent1)
print(f"result: {result}")

result = df.sent0.dot(df.sent2)
print(f"result: {result}")

result = df.sent0.dot(df.sent3)
print(f"result: {result}")
