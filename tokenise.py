import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from string import punctuation

from nltk.collocations import BigramCollocationFinder

customStopWords=set(stopwords.words('english')+list(punctuation))

text = (
  'If you really want to hear about it, the first thing you probably want to know is what my lousy childhood was like,'
  ' and how my parents were occupied and all before they had me, and all that David Copperfield kind of crap,'
  ' but I really don\'t feel like going into it, if you want to know the truth.'
)

sentences = sent_tokenize(text)
words = word_tokenize(text)

wordsWithoutStopwords = [word for word in word_tokenize(text) if word not in customStopWords]

finder = BigramCollocationFinder.from_words(wordsWithoutStopwords)

print(finder.ngram_fd.items())

print(nltk.pos_tag(words))

