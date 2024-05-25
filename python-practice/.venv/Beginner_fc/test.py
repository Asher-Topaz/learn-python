txt = 'but soft what light is yonder window breaks'

#create empty dictionary
counts = dict()

#split txt into a list of words

words = txt.split()

for word in words:
    counts[word] = len(word)

print(counts)