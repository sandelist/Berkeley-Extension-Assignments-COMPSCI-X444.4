# This program performs a bubble sort on a list of integers

status = ''



while status.lower() != 'n':

    input_numbers = input('Please enter a list of integers').split(",")

    int_list = []

    breaker = False
    
    for x in input_numbers:
        try:
            
            int_list.append(int(x))
        
        # This handle value exceptions:
        except:
            
            print('Your input is invalid. Please enter again.')
            
            breaker = True
            break
            
            
    if breaker == False:

        original_list = int_list.copy()

        print_original_list = [str(i) for i in original_list]
        joined_original_list = ", ".join(print_original_list)

        print('\nOriginal List:' + str(joined_original_list))

        sorted_list = []

        status = 'unsorted'

        pass_count = 0

        while status != 'sorted':

            for i in range(0, len(int_list)-1):

                if int_list[i] > int_list[i+1]:
                    temp = int_list[i]
                    int_list[i] = int_list[i+1]
                    int_list[i+1] = temp


            if sorted_list == int_list:
                status = 'sorted'

            if sorted_list != int_list: 
                sorted_list = int_list.copy()

                print_list = [str(i) for i in int_list]
                joined_string = ", ".join(print_list)

                pass_count = pass_count+1
                print('Pass ' + str(pass_count) + ': '+ joined_string)


        print_sorted_list = [str(i) for i in sorted_list]
        joined_sorted_list = ", ".join(print_sorted_list)


        print('\nOriginal List:' + joined_original_list)
        print('Sorted List:' + joined_sorted_list)
        print('Number of Passes:' + str(pass_count))

        status = input('Would you want to sort another list? Y/N')

    if status.lower() == 'n':
        print('Goodbye')