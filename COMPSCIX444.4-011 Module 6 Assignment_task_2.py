temp = ""

while temp != "exit":
    
    temp = input('Please input a temperature (Format: XX Celsius/Fahrenheit) or type "exit" to quit: ')

    if temp.endswith('Celsius') == True:
        try:
            temp_input = float((temp.replace('Celsius','')).strip())
            temp_output = round((temp_input*9/5 + 32),2)
        
            print(str(temp_input) + ' in Celsius = ' + str(temp_output) + ' in Fahrenheit \n')
    
        except ValueError:
            print("I don't understand. Try again. \n")
        
    elif temp.endswith('Fahrenheit') == True:
    
        try:  
            temp_input = float((temp.replace('Fahrenheit','')).strip())
            temp_output = round((5/9*(temp_input - 32)), 2)   
     
            print(str(temp_input) + ' in Fahrenheit = ' + str(temp_output) + ' in Celsius \n')

        except ValueError:
            print("I don't understand. Try again. \n")


    elif temp.lower() == "exit":
        temp = temp.lower()
        print("Goodbye.")
            

    else:
        print("I don't understand. Try again. \n")
