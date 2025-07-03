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

stop_words = ['a', 'an', 'the', 'on', 'of', 'off', 'this', 'is']
tokens = ['the', 'house', 'is', 'on', 'fire']
tokens_without_stopwords = [x for x in tokens if x not in stop_words]
print(tokens_without_stopwords)

import nltk
nltk.download('stopwords')
stop_words = nltk.corpus.stopwords.words('english')

result = len(stop_words)
print(f"result: {result}")

result = stop_words[:7]
print(f"result: {result}")

result = [sw for sw in stop_words if len(sw) == 1]
print(f"result: {result}")

from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS as sklearn_stopwords

result = len(sklearn_stopwords)
print(f"result: {result}")

result = len(stop_words)
print(f"result: {result}")

result = len(set(stop_words).union(sklearn_stopwords))
print(f"result: {result}")

result = len(set(stop_words).intersection(sklearn_stopwords))
print(f"result: {result}")
