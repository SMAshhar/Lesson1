################################## ASSIGNMENT 1 Q 1#######################################

# Excersise 1 : Calculate area of circle from given radius
# x = float(input(print("Please enter the radius of Circle")))
# y = (22/7) * x * x
# print(y)

# Excersise 2 : Identify if the given number is +ve, -ve or zero
# print("\t\t ============================================\t\t")
# x = int(input(print("\t\t Enter a number")))

# if x == 0:
#     print("\t\t The number is zero")
# if x > 0:
#     print("\t\t The number is positive")
# if x < 0:
#     print("\t\t The number is negative")
# print("\t\t ==============================================\t\t")


# Excersise 3 : Divisibility check of 2 numbers

# print("\t\t This program will check if either the provided two numbers are completely divisible")
# print("\t\t ====================================================================================\t\t")
# x = int(input("\t\t Enter the divident"))
# y = int(input("\t\t Enter the devisor"))
# print("\t\t ====================================================================================\t\t")
# z = x % y

# if z == 0:
#     print(f"\t\t Number {x} is completely divisible by number {y}")
# else:
#     print(f"\t\t Number{x} is not completely divisible by number {y}")

# print("\t\t =====================================================================================\t\t")

# # Excersise 4 : DAYS CALCULATOR

# from datetime import date
# f_date = date(2014, 7, 2)
# l_date = date(2014, 7, 11)
# delta = l_date - f_date
# print(delta.days)


# Excersise 5 : CALCULATE VOLUME OF SPHERE VIA RADIUS INPUT

# x = int(input("Enter radius of sphere :"))

# y = (4/3) * (22/7) * x * x * x

# print(f"The Volume for the given radius of a sphere is : {round(y, 2)}")

# Excersize 6 : COPY STRING IN TIME

# x = input("Enter your string : ")
# y = int(input("Enter Number of times it needs copying : "))
# print(x*y)

# Excersise 7 : CHECK IF NUMBER IS EVEN OR ODD

# x = int(input("Enter your desired number : "))

# if x == 0:
#     print("Please enter a non-zero number")
    
# y = x % 2
# if y == 0 and x != 0:
#     print("Number is Even")
# elif y != 0 and x!= 0:
#     print("Number is Odd")

# Excersise 8 : VOWEL TESTER

# x = input("Enter your alphabet : ")

# y = x.lower()

# if y == "a" or y == "e" or y == "i" or y == "o" or y == "u":
#     print(f"{x} is a vowel")
# else:
#     print(f"{x} is not a vowel")

# Excersise 9 : TRIANGLE AREA

#formula for area of a triangle = 1/2 * base * hieght

# base = float(input("Please enter the base of the Triangle : "))
# height = float(input("Please enter the height of the triangle : "))

# Area_of_Triangle = 1/2 * base * height

# print(f"The area of the triangle is : {Area_of_Triangle}")

# Excersise 10 : Calculate interest

# p = float(input("Enter prinscipal value : "))
# r = float(input("Enter rate of interest in percentage : "))
# t = float(input("Enter number of years : "))

# x = p * (1 + ((r/100)/12)) ** (12 * t)

# t = int(t)
# x = round(x, 2)

# print(f"Your total amount after {t} years will be {x}")

# Excersise 11 : EUCLIDEAN DISTANCE

# x1 = int(input("Enter Co-ordinate for x1 : "))
# y1 = int(input("Enter Co-ordinate for y1 : "))
# x2 = int(input("Enter Co-ordinate for x2 : "))
# y2 = int(input("Enter Co-ordinate for y2 : "))

# Euc_distance = (((x2 - x1)**2) + ((y2 - y1)**2))**(1/2) 

# print(f"The euclidean distance between the {x1, y1} and {x2, y2} is {Euc_distance}")

# Excersise 12 : FEET TO CENTIMETER CALCULATOR

# X = float(input("Enter value in feet : "))
# y = X * 30.48
# z = round(y, 2)

# print(f"Your value in centimeter is : {z}")

# Excersise 13 : BODY MASS INDEX CALCULATOR

# w = int(input("Enter your weight in KG : "))
# h = int(input("Enter your height in cm : "))
# h = h/100

# bmi = w/h**2
# bmi = round(bmi, 2)

# print(f"Your BMI is {bmi}")

# Excersise 14 : SUM OF N POSITIVE INTEGERS

# x = int(input("Enter your positive integer"))
# y = 0

# for a in range(x+1):
#     y = y + a
# print(f"Sum of N positive integers is : {y}")

# Excersise 15 : DIGITS SUM OF A NUMBER

# x = int(input("Enter a number greater then zero"))
# sum = 0

# while (x>0):
#     remainder = x % 10
#     sum = remainder + sum
#     x = x // 10

# print(f"The sum of digits of your provided number is {sum}")

# Excersise 16 : DECIMAL TO BINARY CONVERSION

# x = int(input("Enter your number for binary conversion"))
# binary = ""
# y = 0

# while (x>0):
#     remainder = x % 2
#     y = str(remainder)
#     binary = y + str(binary)
#     x = x // 2

# print(f"Your number in binary is {binary}")

# Excersise 17 : BINARY TO DECIMAL CONVERESION

# x = int(input("Enter your number for binary conversion"))

# y = 0
# n = 0
# z = 0

# while (x>0):
#     remainder = x % 10
#     y = remainder * 2**n
#     n += 1
#     z = y +  z
#     x = x // 10
# print(f"Your number from binary to decimal is : {z}")

# Excersise 18 : VOWEL AND CONSONENT COUNTER

# x = input("Enter your text for vowels and consonents counting")
# z = 0
# y = 0

# for a in x:
#     if a == "a" or a == "e" or a == "i" or a == "o" or a == "u":
#         z += 1
#     else:
#         y +=1

# print(f"The statement carried {z} vowels and {y} consonents")

# Excersise 19 : PALINDROME TESTER

# word = input("Enter a word for Palindrome check :")
# word = word.lower()

# rev_word = reversed(word)

# if list(word) == list(rev_word):
#     print("The word is Palindrome")
# else:
#     print("The word is not Palindrome")



# Excersise 20 : COUNT ALPHABATS, NUMERALS AND SPECIAL CHARACTORS

# x = input("Type your entry here : ")

# numeral = 0
# alpha = 0
# special = 0
# space = 0

# alphabets = ["a", "b", 'c', "d", "e", "f", "g", "h", 'i', "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
# numerals = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

# for a in x:
#     if a in numerals:
#         numeral += 1
#     elif a in alphabets:
#         alpha += 1
#     elif a == " ":
#         space += 1
#     else:
#         special += 1

# print("Your entry has following items \n", "Numerals", numeral, "Alphabets", alpha, "Special Charactors", special, "Spaces", space, sep = "\n")


# Excersise 21 : CONSTRUCT THE STAR PATTERN

# for x in range(5):
#     for y in range(x):
#         print("*", end = " ")
#     print("\n")
# for a in range(5, 0, -1):
#     for b in range(a):
#         print("*", end = " ")
#     print(" ")


# Excersise 22 : CONSTRUCT A NUMBER PATTERN


# rows = 5
# for row in range(1, rows+1):
#     for column in range(1, row + 1):
#         print(column, end=' ')
#     print("")
# for row2 in range(4, 0, -1):
#     for column2 in range(1, row2 + 1):
#         print(column2, end = " ")
#     print(" ")

# Excersis 23 : CONSTRUCT THE NUMBER PATTERN

# for x in range(10):
#     for y in range(x):
#         print(x, end = "")
#     print(" ")

t = 5
for x in range(1, t + 1):
    for y in range(1, x + 1):
        print(y, end = ' ')
    print("")
rows = 5
for row in range(1, rows+1):
    for column in range(1, row + 1):
        print(column, end=' ')
    print("")

