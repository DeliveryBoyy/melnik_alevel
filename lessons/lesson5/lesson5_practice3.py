import sys
from operator import methodcaller

word_count = 0
print("Input word to count")
target_word = input()
filename = sys.argv[1]

def counter(word, word_count, target_word):
    if word == target_word:
        word_count += 1
        return word_count
    else:
        return word_count

f = open(filename, 'r')
map(counter, (map(methodcaller("split", " "), f)))

print(word_count)