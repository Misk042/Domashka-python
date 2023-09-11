
num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))
num3 = int(input("Enter number 3: "))
user_select = int(input("1.Maximum of three numbers\n2. Minimum of three numbers\n3.Average of three numbers\n: "))

if user_select == 1:
    print(max(num1, num2, num3))
elif user_select == 2:
    print(min(num1, num2, num3))
elif user_select == 3:
    average = (num1 + num2 + num3) / 3
    print(average)
else:
    print("Incorect numbers")









