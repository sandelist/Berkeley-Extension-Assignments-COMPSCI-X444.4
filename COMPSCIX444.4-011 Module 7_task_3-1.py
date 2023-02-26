# This programme reverses a word using recursion

status = ''

while status.lower() != 'n':

    word = input('Please enter a word: ')
    
    # This list will contain the words in reversed order
    
    reversed_words = []
    n = len(word)

    # This function get an reversed order of the words

    def reverse(n):

        # The function continues unless n is 0, when the list has appended the first word
        if n == 0:
            return reversed_words 

        else:      
            reversed_words.append(word[n-1])   
            return reverse(n - 1)

    print('Original Word: ' + word)
    print('Reversed Word: ' + ''.join(reverse(n)))
    

    status = input('Would you want to reverse another word? Y/N')
    
    if status.lower() == 'n':
        print('Goodbye')