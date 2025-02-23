from models.learn import Learn

l = Learn()
l.start("e2m")

word = l.get_word()
while word != False:
    inp = input(word)
    print(l.check(word,inp))
    word = l.get_word()