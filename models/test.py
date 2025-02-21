from models.learn import Learn

l = Learn("m2e")
while l.get_word() == True:
    print(l.morse_word)
    inp = input("guess")
    print(l.check(inp))