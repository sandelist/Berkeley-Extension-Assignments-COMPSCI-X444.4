# Task 1 - Celsius to Fahrenheit Conversion

celsius_temp = float(input('Please enter a temperature in celsius: '))

fahrenheit_temp = round((celsius_temp*9/5 + 32),2)

print(str(celsius_temp) + ' Celsius equals ' + str(fahrenheit_temp) + ' Fahrenheit')