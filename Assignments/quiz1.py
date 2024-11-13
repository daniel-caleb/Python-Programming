
#               DANIEL-CALEB CHERUIYOT
#                       21/05045
#                   ASSIGNMENT ONE!
#   A python program to read temp in celsius then convert and displays its 
#                   equivalent in Farenheit

# Function to convert Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# Read temperature in Celsius from user
celsius = float(input("Enter temperature in Celsius: "))

# Convert to Fahrenheit
fahrenheit = celsius_to_fahrenheit(celsius)

# Display the result
print(f"{celsius} degrees Celsius is equal to {fahrenheit} degrees Fahrenheit.")
