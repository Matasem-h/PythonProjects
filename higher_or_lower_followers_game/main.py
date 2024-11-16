import art
import random
import game_data
print(art.logo)

game_should_continue = True

while game_should_continue:
    # Option 1 and 2 definitions
    option_one = random.choice(game_data.data)
    option_two = random.choice(game_data.data)

    # Display option 1, VS art, and option 2 to the user
    print(f"{option_one['name']}, a {option_one['description']}, from {option_one['country']}")
    print(art.vs)
    print(f"{option_two['name']}, {option_two['description']}, {option_two['country']}")

    # Ask the user for a guess in follower count
    user_answer = input(f"Who has more followers? Type 'A' or 'B': ").upper()

    # Assign follower count to a variable
    option_one_follower_count = option_one['follower_count']
    option_two_follower_count = option_two['follower_count']

    # Condition for the user answer
    if (user_answer == 'A' and option_one_follower_count > option_two_follower_count or user_answer == 'B'
            and option_two_follower_count > option_one_follower_count):
        print("You are correct. Play again.")
    else:
        print("You are wrong!")
        game_should_continue = False
