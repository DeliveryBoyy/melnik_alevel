import re
import random
slangs = [
    ', yeah!',
    ', this is crazy, I tell ya.',
    ', can U believe this?',
    ', eh?',
    ', aw yea.',
    ', yo',
    '? No way!',
    '. Awesome!'
]

s = "Lorem ipsum dolor sit amet. Mea et habeo doming praesent. Te inani utroque recteque has, sea ne fugit verterem! Usu ei scripta phaedrum, an sed salutatus definiebas? Qui ut recteque gloriatur reformidans. Qui solum aeque sapientem cu. Eu nam nusquam quaestio principes."


s = re.split('[.!?]', s)

print(s)

for i in range(1, len(s)):
    if (i % 2):
        print (s[i] + '.')
    else:
        random_slang_number = random.randint(0,7)
        value = s[i] + slangs[random_slang_number]
        print (value)