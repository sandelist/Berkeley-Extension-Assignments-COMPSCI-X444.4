# This is a program that converts a sentence into Pig Latin:

status = ""

while status != 'n':
    
    sentence =input('Please input your sentence without punctuation:')
    
    sentence_changed = ''

    vowel = ['a','e','i','o','u','A','E','I','O','U']

    words = sentence.split()

    for word in words:

        word_changed = ''

        count = 0

        for i in word:

            # These lines handle the word when the word begins with a vowel

            if count == 0 and i in vowel:
                word_changed = word + 'yay'
                break

            # These lines handle the word when the word begins with a consonant

            elif i in vowel:
                first_vowel_location = count
                word_changed = word[first_vowel_location:] + word[0:first_vowel_location] + 'ay'
                break

            count = count + 1

        if len(word) == count:
            word_changed = '##Invalid##'

        sentence_changed = sentence_changed + ' ' + word_changed

    if '##Invalid##' in sentence_changed:
        print('You sentence contains a word without vowel.')
        
    else:
        print(sentence_changed[1:])
        
        status = input('Convert another sentence? Please enter: Y/N').lower()
        
        if status == 'n':
            print('Goodbye')