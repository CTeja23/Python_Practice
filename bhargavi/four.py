def textPreprocessing(text):
    p_marks = ['.','?','!',':',';','-','[',']','{','}','(',')','’',',','"',]
    stop_words = ['i', 'a', 'about', 'am', 'an', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'how', 'in', 'is', 'it', 'of', 'on', 'or', 'that', 'the', 'this', 'to', 'was', 'what', 'when', 'where', 'who', 'will', 'with']

    line = ""
    for letter in text:
        if letter not in p_marks:
            line += letter
    line = line.split()

    words = [word.lower() for word in line if word not in stop_words ]
    output = []
    for i in words:
        if i.endswith('ing'):
            i = i.removesuffix('ing')
            output.append(i)
        elif i.endswith('ed'):
            i = i.removesuffix('ed')
            output.append(i)
        elif i.endswith('s'):
            i = i.removesuffix('s')
            output.append(i)
        else:
            output.append(i)
    return output


print(textPreprocessing("I think, therefore I am."))
