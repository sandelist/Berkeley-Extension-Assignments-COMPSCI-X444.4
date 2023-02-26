# This program sorts a list of integers in ascending order and return their mean

# This function performs insertion sort

def insertion_sort(numbers):

    print('Original List: ', str(numbers))
    status = ''

    count = 0

    
    while status != 'sorted':
        for i in range(0, len(numbers)-1):

            first = i

            second = i+1

            if numbers[first] > numbers[second]:
                temp = numbers[second]
                numbers[second] = numbers[first]
                numbers[first] = temp

                count = count + 1
                print('Swap ' + str(count) +': ' + str(numbers))

                break

        else:
            status = 'sorted'

    print('Sorted List: ', str(numbers))
    
    return numbers


# This function gets the mean of numbers entered by the number

def calculate_mean(numbers):
    mean = sum(numbers)/len(numbers)
    print('Mean Value: ' + str(mean))


status = ''

while status.lower() != 'n':

    input_numbers = input('Please enter a list of comma separated numbers')

    # Delete the last item if it is a comma. Users may end the list with a comma. 
    if input_numbers[-1] == ',':
        input_numbers = input_numbers[:-1]

    input_numbers_list = input_numbers.split(",")

    input_numbers_list_int = []
     
    value_error = 'N'
    
    for x in input_numbers_list:
        
        try:
            input_numbers_list_int.append(int(x))
            
        # This checks whether the input by the users contains values other than numbers
        
        except:
            
            print('You input is valid.')
            value_error = 'Y'
            break
    
    if value_error == 'N':
        calculate_mean(insertion_sort(input_numbers_list_int))
    
    status = input('Would you want to sort another list? Y/N')
    
    if status.lower() == 'n':
        print('Goodbye')