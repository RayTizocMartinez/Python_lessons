def piggify_word(latinword):
    piglatin=[]
    vowels = ('a', 'e', 'i', 'o', 'u')
    if latinword[0] not in vowels:
        for w in latinword[1: ]:
            piglatin.append(w)
        piglatin.append(latinword[0] + 'ay')
    else:
        piglatin.append(latinword[1:])
        piglatin.append(latinword[0] + 'say')



    return ''.join(piglatin)

print(piggify_word('goodbye'))


def piggify_string(latin_sentance):
    piglatin_phrase=latin_sentance.split(' ')
    piglattin_post = []
    for x in piglatin_phrase:
        #print(piggify_word(x))
        piglattin_post.append(piggify_word(x))




print(piggify_string('life is a bitch'))
