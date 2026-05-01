text = (
    'Etiam tincidunt neque erat, quis molestie enim imperdiet vel. '
    'Integer urna nisl, facilisis vitae semper at, dignissim vitae libero'
)

words = text.split()
fin_words = []

for word in words:
    if ',' in word or '.' in word:
        new_word = word[:-1] + 'ing' + word[-1]
    else:
        new_word = word + 'ing'
    fin_words.append(new_word)
print(' '.join(fin_words))
