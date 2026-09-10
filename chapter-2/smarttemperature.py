# question- Take input in celsius and print its equivalent in fahrenheit and kelvin.(use ecpliciet type conversion and arethmatic operators)
# Formula (1.Fahrenheit = (C*9/5)+32),(2.Kelvin = C + 273.15)

celsius= int(input("Enter your number:"))
fahrenheit=(celsius*9/5)+32
kelvin = celsius+273.15
print("Fahrenheit is:", fahrenheit)
print("Kelvin is:", kelvin)
print(type(kelvin))
