
number1 = int(input("Enter the number of meters: "))
number2 = int(input("Measurement:\n1.Meters\n2.Mile\n3.Inch\n4.Yard\n : "))

if number2 == 1:
    print(number1)
elif number2 == 2:
    print(number1 * 0.000621371)
elif number2 == 3:
    print(number1 * 39.370)
elif number2 == 4:
    print(number1 * 1.0936)
else:
    print("Incorect number")