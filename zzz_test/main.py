# This is a simple page to test out new stuff that I'm learning.

# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# squared_numbers = [n ** 2 for n in numbers]
# print(squared_numbers)


# list_of_strings = ['9', '0', '32', '8', '2', '8', '64', '29', '42', '99']
# numbers = [int(num) for num in list_of_strings]
# result = [num for num in numbers if num % 2 == 0]
# print(result)


##################################################################################################################
# This is a shorter version of the one below.
# missing_states = [state for state in all_states if state not in guessed_states]


# The one below
# missing_states = []
# for state in all_states:
#     if state not in guessed_states:
#         missing_states.append(state)
##################################################################################################################


# Dictionary Comprehension from another dictionary
# new_dict = {new_key: new_value for (key, value) in dict.items() if test}


# import random
# names = ['Alex', 'Beth', 'Caroline', 'Dave']
# students_scores = {student:random.randint(1, 100) for student in names}
# passed_students = {student:score for (student, score) in students_scores.items() if score >= 60}

# from tkinter import *
#
# window = Tk()
# window.title("My First GUI Program")
# window.minsize(width=500, height=300)
# window.config(padx=100, pady=100)
#
#
# def button_clicked():
#     print("I got clicked")
#     new_text = input.get()
#     my_label["text"] = new_text

# # Label
# my_label = Label(text="I Am a Label", font=("Arial", 24, "italic"))
# my_label.config(text="New Text")
# my_label.grid(column=0, row=0)
# my_label.config(padx=50, pady=50)

# # Button
# button = Button(text="Click Me", command=button_clicked)
# button.grid(column=1, row=1)
# new_button = Button(text="New Button")
# new_button.grid(column=2, row=0)

# # Entry
# input = Entry(width=10)
# print(input.get())
# input.grid(column=3, row=2)
#
#
# window.mainloop()


# # try except
# try:
#     file = open("a_file.txt")
#     a_dictionary = {"key": "value"}
#     print(a_dictionary["key"])
# except FileNotFoundError:
#     file = open("a_file.txt", "w")
#     file.write("Something")
# except KeyError as error_message:
#     print(f"The key {error_message} does not exist")
# else:
#     content = file.read()
#     print(content)
# finally:
#     raise TypeError()
#
#
# # Raise
# height = float(input("Height: "))
# weight = float(input("Weight: "))
#
# if height > 3:
#     raise ValueError("Human heights should not be over 3m.")
#
# bmi = weight / height ** 2
# print(bmi)
#

# # KeyError
# a_dictionary = {"key": "value"}
# value = a_dictionary["non_existent_key"]

# # IndexError
# fruit_list = ["Apple", "Banana", "Pear"]
# fruit = fruit_list[3]

# # TypeError
# text = "abc"
# print(text + 5)


facebook_posts = [
    {'Likes': 21, 'Comments': 2},
    {'Likes': 13, 'Comments': 2, 'Shares': 1},
    {'Likes': 33, 'Comments': 8, 'Shares': 3},
    {'Comments': 4, 'Shares': 2},
    {'Comments': 1, 'Shares': 1},
    {'Likes': 19, 'Comments': 3}
]


def count_likes(posts):

    total_likes = 0
    for post in posts:
        try:
            total_likes = total_likes + post['Likes']
        except KeyError:
            pass

    return total_likes


count_likes(facebook_posts)



