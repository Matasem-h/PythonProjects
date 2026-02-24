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
# int_1 = 1
# int_2 = 2
# print("Your two numbers are " + str(int_1) + " and " + str(int_2) + ".")
#
# int_3 = int_1 + int_2
# print(str(int_1) + " plus " + str(int_2) + " equals " + str(int_3) + ".")
#
# int_3 = int_1 - int_2
# print(str(int_1) + " minus " + str(int_2) + " equals " + str(int_3) + ".")
#
# int_3 = int_1 * int_2
# print(str(int_1) + " times " + str(int_2) + " equals " + str(int_3) + ".")
#
# int_3 = int_1 / int_2
# print(str(int_1) + " divided by " + str(int_2) + " equals " + str(int_3) + ".")


# def my_first_function():
#     print("I can't believe I'm in a function!")
#
#
# print("I'm not in a function!")
# my_first_function()
# print("I'm not in a function anymore!")


# if this_new_variable == 5:
#     print("In scope!")
#
# this_new_variable = 0


# print("Welcome to my program!")
# print("I'm excited to see if the variable is in scope!")
#
# if this_new_variable == 5:  # It's not in scope.
#     print("In scope!")
#
# this_new_variable = 0
# print("We're almost finished!")
# print("And... now we're done.")

# def my_function():
#     print("Nice function!")
#     my_variable = "I love functions!"
#     print("my_variable" + my_variable)
#
#
# print("Starting program...")
# my_function()
# if my_variable == "Quit":  # my_variable is defined inside a function, so we get NameError.
#     print("Ending program...")


# def my_function():
#     my_variable = "Inside of the function"
#     print("my_variable = " + my_variable)
#
#
# my_variable = "Outside of the function"
# print("my_variable = " + my_variable)
# my_function()
# print("my_variable = " + my_variable)


# def my_function():
#     print("In my function")
#
#     def my_nested_function():
#         print("In my nested function")
#         print("Exiting my nested function")
#
#     print("About to call the nested function")
#     my_nested_function()
#     print("Finishing call to nested function")
#     print("Exiting my function")
#
#
# print("About to call my function")
# my_function()
# print("Finished call to my function")


# x = 1
# def my_function():
#     x = 10
#     print("In my function, x = " + str(x))
#
#     def my_nested_function():
#         x = 100
#         print("In my nested_func x = " + str(x))
#
#     my_nested_function()
#
#
# my_function()
# print("Outside of functions, x = " + str(x))

# x = 1
# def my_function():
#     global x
#     x = 10
#     print("In my_function, x=" + str(x))
#
#     def my_nested_function():
#         global x
#         x = 100
#         print("In my_nested_function, x=" + str(x))
#
#     my_nested_function()
#     print("At the end of my_function, x=" + str(x))
#
#
# my_function()
# print("Outside of functions, x=" + str(x))


# x = 1
# def my_function():
#     x = 10
#     print("In my_function, x=" + str(x))
#
#     def my_nested_function():
#         nonlocal x
#         x = 100
#         print("In my_nested_function, x=" + str(x))
#
#     my_nested_function()
#     print("At the end of my_function, x=" + str(x))
#
#
# my_function()
# print("Outside of functions, x=" + str(x))


    # Function Arguments
# def add_three_numbers(a, b, c):
#     the_sum = a + b + c
#     print("The sum of " + str(a) + ", " + str(b) + ", and " + str(c) + " " + "is: " + str(the_sum))
#
#
# add_three_numbers(1, 2, 3)       # Valid
# add_three_numbers(1, 2, 3, 4)    # TypeError: add_three_numbers() takes 3 positional arguments but 4 were given
# add_three_numbers(1, 2,)            # TypeError, missing 1 required positional argument: 'c'


# def person_info(name, phone, address, age):
#     print("Name: " + name)
#     print("Phone: " + phone)
#     print("Address: " + address)
#     print("Age: " + str(age))
#
#
# person_info("Alyssa Reinford", "423-192-2311", "152 Wander Lane", 23)
# person_info(name="Rean Schwarzer", address="51 Cosmo Drive", phone="321-910-2238", age=28)


# def do_math(a, b=1, c=2, d=3):
#     result = a + b + c + d
#     print("Sum is: " + str(result))
#     result = a * b * c * d
#     print("Product is: " + str(result))
#
# do_math(1)
# do_math(1, 5)
# do_math(1, 5, 10)
# do_math(1, 5, 10, 20)


# def return_one_thing(a, b):
#     result = a + b
#     return result
#
#
# def return_two_things(a, b):
#     result1 = a + b
#     result2 = a - b
#     return result1, result2
#
#
# print(return_one_thing(5, 6))
# print(return_two_things(5, 6))  # prints (11, -1) enclosed by parentheses, because the function returns a tuple.


# x = 1
# def outer():
#     x = 10
#     print("Outer", x)
#
#     def inner():
#         x = 100
#         print("Inner", x)
#
#     inner()
#     print("Outer end:", x)
#
#
# outer()
# print("Global:", x)


# def person_info(name, phone, address, age):
#     print(f"Name: {name}")
#     print(f"Phone: {phone}")
#     print(f"Address: {address}")
#     print(f"Age: {age}")
#
#
# person_info("Alyssa Reinford", "423-192-2311", "152 Wander Lane", 23)
#
# person_info(address="51 Cosmo Drive", name="Rean Schwarzer", phone="321-910-2238", age=28)

# Unit 5 --- Errors and Exceptions ---

# value = int(input())
# if value == 10  # Missing colon :
#     print("You entered 10!")  # SyntaxError, due to missing colon

# value = int(input())
# value == 10:
#     print("You entered 10!")

# value = input("Enter a number: ")
# result = str(5 / int(value))
# print("5 divided by " + value + " = " + result)         # If input = 0 ---> ZeroDivisionError

# file_name = input()
# my_file = open(file_name, "r")
# print(my_file.read())
# my_file.close()

    # try - except

# try:
#     value = input("Enter a number: ")
#     result = str(5 / int(value))
#     print("5 divided by " + value + " = " + result)
# except ZeroDivisionError:
#     print("You tried to divide by zero!")
# print("We're now at the end of the program.")

# try:
#     file_name = input()  # if the user enters a valid filename
#     my_file = open(file_name, "r")
#     print(my_file.read())
#     my_file.close()
# except FileNotFoundError:  # if the file does not exist
#     print("File not found")
# print("End of program")

# try:
#     my_variable = 10 / 10
#     print(my_variable)
# except ZeroDivisionError:
#     print("Divided by zero!")
# finally:
#     print("Here's our finally block...")
# print("End of program")

# try:
#     raise ZeroDivisionError
# finally:
#     print("Here's out finally block...")
# print("End of program")

# import logging
#
# logging.basicConfig(level=logging.DEBUG)
#
# logging.debug("Debug is the lowest log level")
# logging.info("Info is the second lowest log level")
# logging.warning("Warning is the third level")
# logging.error("Error is the fourth level")
# logging.critical("Critical is the fifth and highest level")

# import logging
#
# logging.basicConfig(filename="mylog.log", filemode="w", level=logging.DEBUG)    #
#
# logging.debug("Debug is the lowest log level")
# logging.info("Info is the second lowest log level")
# logging.warning("Warning is the third level")
# logging.error("Error is the fourth level")
# logging.critical("Critical is the fifth and highest level")

# import logging
# logging.basicConfig(format="%(asctime)s: %(message)s")
# logging.critical("My log message")


# Unit 6 Code

# from math import floor
#
# print(floor(6.5))
#
#
# def floor(a):
#     if a == 1:
#         return "First Floor"
#     elif a == 2:
#         return "Second Floor"
#     elif a == 3:
#         return "Third Floor"
#
#
# print(floor(2))

my_str = "Hello, World!"
print(my_str)


def print_it_x_times(str, x):
    a = 0
    while a < x:
        print(str)
        a += 1


print_times = 5
print_it_x_times("Hello again, World!", print_times)











































































