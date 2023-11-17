import random
import pyttsx3

engine = pyttsx3.init()


def game():
    user_wins = 0
    computer_wins = 0
    options = ["rock", "paper", "scissors", "fire"]
    while True:
        user_input = input("Type Rock/Paper/Scissors/fire or Q or quit to quit: ").lower()
        if user_input == "q" or user_input == "quit":
            break
        if user_input not in options:
            continue

        random_number = random.randint(0, 3)

        computer_pick = options[random_number]
        print("Computer picked", computer_pick + ".")

        if user_input == "rock" and computer_pick == "scissors" or computer_pick == "rock":
            print("You won!")
            user_wins += 1

        elif user_input == "paper" and computer_pick == "rock":
            print("You won!")
            user_wins += 1

        elif user_input == "scissors" and computer_pick == "paper":
            print("You won!")
            user_wins += 1

        elif user_input == "fire" and computer_pick in options[:-1]:
            print("You won!")
            user_wins += 1

        else:
            print("You lost!")
            computer_wins += 1

        x = f"You won {user_wins} times. The computer won {computer_wins} times."
        print(x)

    print("Goodbye!")

    engine.say(x)
    engine.save_to_file(x, 'test.mp3')
    engine.runAndWait()


game()
