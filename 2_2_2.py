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

import re
sentence = """Thomas Jefferson began building Monticello at the age of 26."""

pattern = re.compile(r"([-\s,.!?])+")
tokens = pattern.split(sentence)
print(f"tokens[-10:]: {tokens[-10:]}")

result = [x for x in tokens if x and x not in '- \t\n.,!?']
print(f"result: {result}")

result = list(filter(lambda x: x if x not in '- \t\n.,!?' else None, tokens))
print(f"result: {result}")

from nltk.tokenize import RegexpTokenizer
tokenizer = RegexpTokenizer(r'\w+|$[0-9.]+|\S+')
result = tokenizer.tokenize(sentence)
print(f"result: {result}")

from nltk.tokenize import TreebankWordTokenizer
sentence = """Monticello wasn't designated as UNESCO world Heritage Site until 1987."""
tokenizer = TreebankWordTokenizer()
result = tokenizer.tokenize(sentence)
print(f"result: {result}")
