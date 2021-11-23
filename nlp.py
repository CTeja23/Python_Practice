def textPreprocessing(text):
    p_words = ['.','?','!',':',';','-','[',']','{','}','(',')','’',',','"',]
    s_words = ['i', 'a', 'about', 'am', 'an', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'how', 'in', 'is', 'it', 'of', 'on', 'or', 'that', 'the', 'this', 'to', 'was', 'what', 'when', 'where', 'who', 'will', 'with']

    new_line = ""

    for letter in text:
        if letter not in p_words:
            new_line += letter

    new_line = new_line.split()

    new_words = []

    for word in new_line:
        word = word.lower()
        if word not in s_words:
            new_words.append(word)


    checked_words = []

    for i in new_words:
        if i.endswith('ing'):
            i = i.removesuffix('ing')
            checked_words.append(i)
        elif i.endswith('ed'):
            i = i.removesuffix('ed')
            checked_words.append(i)
        elif i.endswith('s'):
            i = i.removesuffix('s')
            checked_words.append(i)
        else:
            checked_words.append(i)

    return checked_words


print(textPreprocessing("I think, therefore I am."))
