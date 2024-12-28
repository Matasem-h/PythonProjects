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

import tkinter

window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)

# Label

my_label = tkinter.Label(text="I Am a Label", font=("Arial", 24, "italic"))
my_label.pack()















window.mainloop()
