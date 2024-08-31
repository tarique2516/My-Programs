import random

# This function is to get computer choice from random module
def auto_computer_choice():
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)

# This is the function to determine the winner!
def winner(users_choice, computer_choice):

    if users_choice == computer_choice:
        return "Game is Tie!"
    
    elif(users_choice == "rock" and computer_choice == "scissors") or \
        (users_choice == "paper" and computer_choice == "rock") or \
        (users_choice == "scissor" and computer_choice == "paper"):
        return "You Won The Game!"
    else:
        return "Computer win!"
    

# Main Game loop start here
print("Welcome to Rock, Paper, Scissors")
def play_game():
    
    users_choice = input("Enter rock, paper, scissors: ").lower()

    if users_choice != "rock" and users_choice != "paper" and users_choice != "scissors":
        print("Wrong choice! You need to choose from rock, paper, or scissors.")
        return

    computer_choice = auto_computer_choice()
    print(f"Computer choose: {computer_choice}")

    result = winner(users_choice, computer_choice)
    print(result)
    return result
play_game()

def save_result(result):
    with open("game_results.txt", "b") as file:
        file.write(result + "\n")