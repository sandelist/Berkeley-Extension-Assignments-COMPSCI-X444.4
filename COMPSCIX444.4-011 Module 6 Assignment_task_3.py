import RPi.GPIO as GPIO

import time

GPIO.setmode(GPIO.BOARD)

GPIO.setup(11, GPIO.OUT)
           
status = ''

error_now = False
   
while status != 'N':

   
    led_text = input('Convert your text to morse code:')

    mores_code = []

    # This dictionary was taken from https://www.geeksforgeeks.org/morse-code-translator-python/
    code = { 'A':'.-', 'B':'-...',
            'C':'-.-.', 'D':'-..', 'E':'.',
            'F':'..-.', 'G':'--.', 'H':'....',
            'I':'..', 'J':'.---', 'K':'-.-',
            'L':'.-..', 'M':'--', 'N':'-.',
            'O':'---', 'P':'.--.', 'Q':'--.-',
            'R':'.-.', 'S':'...', 'T':'-',
            'U':'..-', 'V':'...-', 'W':'.--',
            'X':'-..-', 'Y':'-.--', 'Z':'--..',
            '1':'.----', '2':'..---', '3':'...--',
            '4':'....-', '5':'.....', '6':'-....',
            '7':'--...', '8':'---..', '9':'----.',
            '0':'-----', ', ':'--..--', '.':'.-.-.-',
            '?':'..--..', '/':'-..-.', '-':'-....-',
            '(':'-.--.', ')':'-.--.-', ' ':'/'}

    for x in led_text:

        try:
           
            letter = code[x.upper()]
           
            for j in letter:
                if j == '.':
                    print('.')  # On for 1 seconds
                    GPIO.output(11, True)
                    time.sleep(1)
                   
               
                elif j == '-': 
                    print('-') # On for 3 seconds
                    GPIO.output(11, True)
                    time.sleep(2)
               
                elif j == '/':
                    # Pause for 1 second
                    GPIO.output(11, False)
                    time.sleep(1)
                   
                # Pause for 1 second
                print('Pause')
                GPIO.output(11, False)
                time.sleep(1)
                   
                   
            # Pause for 2 seconds
            GPIO.output(11, False)
            time.sleep(2)            
       
        except KeyError:
               
            print('You input an invalid character. Please try again')
           
            status = ''
           
            error_now = True
            break
   
    if error_now == False:

        status = input('Convert another text? Y/N')
        
    if status == 'N':
        print('Good bye')
