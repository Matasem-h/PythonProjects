# Unit 1 --- sss ---
# print("Hello, World!")       # Hello, World! In Python




























# Unit 2 --- Strings ---

# my_file = open("my_file.txt", "w")
# my_file.write("I am writing to a file in Python!!!")
# my_file.close()

# my_file = open("my_file.txt", "r")
# print(my_file.read())
# my_file.close()


# my_string = "He said 'Hi'"
# print(my_string)

# my_string = "He said \"Hello\"\nNew line here."
# print(my_string)

# my_string = r"C:\folder\file.txt\n"
# print(my_string)

# my_string = """Line one
# line two
# line three"""
# print(my_string)

# my_string = "My name is {name} and I'm {age} years old.".format(name="Joe", age=28)
# print(my_string)

# name = "Joe"
# age = 28
# my_string = "My name is {name} and I'm {age} years old.".format(name=name, age=age)
# print(my_string)

# s = "Hello, World!"
# print(s[::2])

# list = [1, 2.6, "Bob"]
# list.append("Janet")
# list.insert(2, 99)
# list.remove(2.6)
# x = list.count(1)
# print(list, x)


# Unit 3 --- Assignment and Expressions ---
    # PEMDAS
# e = 2 ** 2 * 3 / 4 + 6 - 7        # 2.0
# e = 2 ** 2 * 3 / (4 + 6 - 7)      # 4.0
# e = 2 ** (2 * 3) / 4 + 6 - 7      # 15.0
# print(e)

    # Chained Assignment
# a = b = c = d = 10        # prints 10 10 10 10
# print(a, b, c, d)
# a = b = c = d + 5 = 10      # SyntaxError: cannot assign to expression

# print("Print is amazing!", 5, 7.2, 0x65)

    # Input
# print("Type a value:")
# my_variable = input()
# print("You entered:", my_variable)
# print("Try it again:")
# my_variable = input()
# print("You entered: ", my_variable)

# my_string = input()
# my_int = input()
# my_float = input()
# print(type(my_string))
# print(type(my_int))
# print(type(my_float))

# int("65")			# 65
# float("23.52")	# 23.52
# str(67)			# "67"
# int("Hi")			# ValueError

    # If-Statement
# print("Enter a number")
# my_number = input()
#
# if int(my_number) < 10:
#     print("Your number is less than 10!")
#     print(my_number)
#
# else:
#     print("Your number is more than 10!")
#     print(my_number)
#
# print("We're done!")

#     # Elif-Statement
# print("Enter a number:")
# my_number = int(input())
#
# if my_number < 0:
#     print("Your number is negative.")
#
# elif my_number == 0:
#     print("Your number is zero.")
#
# else:
#     print("Your number is positive.")
#
# print(my_number)

    # Loop
# for x in range(5, 10, 1):       # 0 - 9
#     print(x)

# for x in range(5, 10, 2):       # Start, Stop, Step Parameters
#     print(x)

# my_players = ["Franz Beckenbauer", "Gerd Muller", "Lothar Matthaus", "Manuel Neuer"]
# for x in range(4):
#     print("Player " + str(x + 1) + ": " + my_players[x])


# my_players = ["Franz Beckenbauer", "Gerd Muller", "Lothar Matthaus", "Manuel Neuer"]
# x = 0
# while x < 4:
#     print("Player " + str(x + 1) + ": " + my_players[x])
#     x += 1
# print("End of roster")

# my_players = ["Franz Beckenbauer", "Gerd Muller", "Lothar Matthaus", "Manuel Neuer"]
# for x in range(4):
#     if x > 1:
#         break
#     print("Player " + str(x + 1) + ": " + my_players[x])
# print("End of roster")

# for x in range(2, 21, 2):
#     print(x)

# print("Enter a number")
# num = int(input())
#
# if num < 10:
#     print("Less than 10!")
#     print(num)
# else:
#     print("More than 10!")
#     print(num)
# print("We're done!")


# for i in range(5, 10, 2):			# 0 1 2 3 4 5 6 7 8 9
#     print(i)


# players = ["Franz Beckenbauer", "Gerd Muller", "Lothar Matthaus", "Manuel Neuer"]
#
# for i in range(4):
#     print(f"player {i + 1}: {players[i]}")

# Iterator
# my_list = [4, 8, 15, 16, 23, 42]
# my_iterator = iter(my_list)
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))

# my_list = [4, 8, 15, 16, 23, 42]
# my_iterator = iter(my_list)
# for x in my_iterator:
#     print(x)







# Unit 4 --- Functions ---
int_1 = 1
int_2 = 2
print("Your two numbers are " + str(int_1) + " and " + str(int_2) + ".")

int_3 = int_1 + int_2
print(str(int_1) + " plus " + str(int_2) + " equals " + str(int_3) + ".")

int_3 = int_1 - int_2
print(str(int_1) + " minus " + str(int_2) + " equals " + str(int_3) + ".")

int_3 = int_1 * int_2
print(str(int_1) + " times " + str(int_2) + " equals " + str(int_3) + ".")

int_3 = int_1 / int_2
print(str(int_1) + " divided by " + str(int_2) + " equals " + str(int_3) + ".")

















# Unit 5 Code



















# Unit 6 Code



















