# # domashka 2
# num1 = int(input("Enter number 1: "))
# num2 = int(input("Enter number 2: "))
# num3 = int(input("Enter number 3: "))
# user_select = int(input("1.Maximum of three numbers\n2. Minimum of three numbers\n3.Average of three numbers\n: "))
#
# if user_select == 1:
#     print(max(num1, num2, num3))
# elif user_select == 2:
#     print(min(num1, num2, num3))
# elif user_select == 3:
#     average = (num1 + num2 + num3) / 3
#     print(average)
# else:
#     print("Incorect numbers")
#
#
#
# number1 = int(input("Enter the number of meters: "))
# number2 = int(input("Measurement:\n1.Meters\n2.Mile\n3.Inch\n4.Yard\n : "))
#
# if number2 == 1:
#     print(number1)
# elif number2 == 2:
#     print(number1 * 0.000621371)
# elif number2 == 3:
#     print(number1 * 39.370)
# elif number2 == 4:
#     print(number1 * 1.0936)
# else:
#     print("Incorect number")

# Domashka 3

# №1
#
# v1

week = ["Понеділок", "Вторник", "Середа", "Четвер", "П'ятниця", "Субота", "Неділя"]
numbers = int(input("Вкажіть цифрою день тиждня: "))

if numbers == 1:
    print(week[0])
elif numbers == 2:
    print(week[1])
elif numbers == 3:
    print(week[2])
elif numbers == 4:
    print(week[3])
elif numbers == 5:
    print(week[4])
elif numbers == 6:
    print(week[5])
elif numbers == 7:
    print(week[6])
else:
    print("Вказано невірне значення!")

# v2

try:
    user_select = int(input("Вкажіть цифрою (1-7) день тиждня: "))

    if user_select == 1:
        print("Понеділок")
    elif user_select == 2:
        print("Вівторок")
    elif user_select == 3:
        print("Середа")
    elif user_select == 4:
        print("Четвер")
    elif user_select == 5:
        print("П'ятниця")
    elif user_select == 6:
        print("Субота")
    elif user_select == 7:
        print("Неділя")
    else:
        print("Невірне значення!")

except Exception as e:
    print(f"Error: {e}")



####

# №2

print("Уведіть два числа щоб вияснити чи рівні вони, якщо ні вони стануть за зростанням")
number_1 = int(input("Перше число: "))
number_2 = int(input("Друге число : "))
number_3 = [number_1, number_2]
if number_1 == number_2:
    print("Числа рівні")
elif number_1 != number_2:
    print(sorted(number_3))
else:
    print("none")


# №3

n1 = int(input("Enter first numbers: "))
n2 = int(input("Enter second numbers: "))
diya = input("Enter +, -, *, /: ")

if diya == "+":
    print(n1 + n2)
elif diya == "-":
    print(n1 - n2)
elif diya == "*":
    print(n1 * n2)
elif diya == "/":
    print(n1 / n2)
else:
    print("Incorrect action")










