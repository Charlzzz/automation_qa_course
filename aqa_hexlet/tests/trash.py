def pig_it(text):
    words = []
    text = text.split()
    for i in text:
        print(words.append(i[1:]+i[0]+"ay"))
    return " ".join(words)


pig_it('Pig latin is cool')