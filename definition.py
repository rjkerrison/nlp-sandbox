import nltk
from nltk.corpus import wordnet
from nltk.wsd import lesk

def determine_sense(tokens, words):
  for word in words:
    sense = lesk(tokens, word)

    print(sense, sense.definition())

def show_sense_vectors(tokens, words):
  context = set(tokens)
  print(context)

  for word in words:
    print(word)
    context_gen = ((context.intersection(ss.definition().split()), ss) for ss in wordnet.synsets(word))
    context_gen_len = ((-len(a), a, b) for (a, b) in context_gen)
    for a_len, a, x in sorted(context_gen_len):
      print(a_len, a, x.definition())

def the_whole_thing(phrase, words):
  tokens = nltk.word_tokenize(phrase)

  print(r'{:->10}{:-<90}'.format('', phrase))
  print('Determined senses for ', words)
  determine_sense(tokens, words)

  show_sense_vectors(tokens, words)

the_whole_thing('Harry stood on the bank of the river. He could see a bear catching fish.', ['bear', 'bank'])
the_whole_thing('Harry stood on the bank of the river from which he could see a bear catching fish.', ['bear', 'bank'])
the_whole_thing('As he walked along the river, Harry stopped to gaze at the other bank, where a bear was quietly looking for fish.', ['bear', 'bank'])
the_whole_thing('Harry saw a brown bear on the grassy bank.', ['bear', 'bank'])
the_whole_thing('Harry worked at the bank during the bear market.', ['bear', 'bank'])
