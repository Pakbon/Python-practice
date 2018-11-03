'''simple markov generator'''
from numpy.random import choice

with open('markov.txt') as tesla:
    text = tesla.readline()
woorden = text.split()

def make_pairs(words):
    for i in range (len(words)-1):
        yield (words[i], words[i+1])
    
pair = make_pairs(woorden)
dictio = {}
for word_1, word_2 in pair:
    if word_1 in dictio.keys():
        dictio[word_1].append(word_2)
    else:
        dictio[word_1] = [word_2]

start = choice(woorden)
chain = [start]
n_words = 120

for i in range(n_words):
    chain.append(choice(dictio[chain[-1]]))
zinnen = ' '.join(chain)
print(zinnen)