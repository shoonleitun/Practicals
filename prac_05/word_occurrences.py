WORDS = {}
sentence = input("Enter a sentence : ")

sen = sentence.split()

for i in sen:
    word_count = WORDS.get(i,0)
    WORDS[i] = word_count + 1

    sen = list(WORDS.keys())
    sen.sort()


max_length = max((len(sen) for i in sen))
for i in sen:
    print("{:{}} : {}".format(i, max_length, WORDS[i]))
