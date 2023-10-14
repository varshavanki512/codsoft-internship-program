import random
# Function to determine the winner


def determine_winner(user_choice, computer_choice):

    if user_choice == computer_choice:
        return "It's a tie!"
    elif (
        (user_choice == "rock" and computer_choice == "scissors")
        or (user_choice == "scissors" and computer_choice == "paper")
        or (user_choice == "paper" and computer_choice == "rock")
    ):
        return "You win!"
    else:
        return "Computer wins!"
# Function to play a round of the game


def play_round():

    user_choice = input("Choose rock, paper, or scissors: ").lower()
    computer_choice = random.choice(["rock", "paper", "scissors"])
    print(f"You chose {user_choice}")
    print(f"Computer chose {computer_choice}")
    result = determine_winner(user_choice, computer_choice)
    print(result)
    return result
# Function to play the game multiple times


def play_game():
    user_score = 0
    computer_score = 0
    while True:
        result = play_round()

        if "You win" in result:
            user_score += 1
        elif "Computer wins" in result:
            computer_score += 1
        print(f"Score - You: {user_score} | Computer: {computer_score}")
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            break
    print("Thanks for playing!")
# Start the game


print("Welcome to Rock-Paper-Scissors!")
play_game()
