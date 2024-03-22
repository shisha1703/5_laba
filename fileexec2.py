def www():
    with open('file1.txt', 'r+') as f1:
        words = []

        for line in f1:
            for word in line.split():

                if len(word) < 2:
                    new_word = word[0]
                    words.append(new_word)

                elif len(word) < 3:
                    new_word = word[1] + word[0]
                    words.append(new_word)

                else:
                    new_word = word[1] + word[0] + word[2].upper() + word[3:]
                    words.append(new_word)
    with open('file2.txt', 'w+') as f2:
        f2.write(' '.join(words))