# This program calculates whether a Martian year was a leap year

year = "" #set initial value for year variable

while year != "exit":
    
    year = input("Enter a Year or type Exit: ")
      
    if year.isnumeric():

        year = int(year)

        if year % 2 != 0 or year%10 == 0:
            print('This is an leap year on Mars. \n')
    
        else:
            print('This is not a leap year on Mars. It is a normal year.\n')

    else:
        
        if year.lower() == "exit":
            year = year.lower()
            print("Goodbye.")
            
        else:    
            print("I don't understand. Try again.\n")