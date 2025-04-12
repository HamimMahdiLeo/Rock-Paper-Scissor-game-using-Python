from random import choice

print("""
Rock, Paper, Scissors Game
Instructions:
1. Enter 1 for Rock
2. Enter 2 for Paper
3. Enter 3 for Scissors
""")

def result(player, computer):
    
    choices = {1: "Rock", 2: "Paper", 3: "Scissors"}

    
    print(f"You chose: {choices[player]}")
    print(f"Computer chose: {choices[computer]}")

    if player == computer:
        print("Result: TIE")
    elif (player == 1 and computer == 3) or \
         (player == 2 and computer == 1) or \
         (player == 3 and computer == 2):
        print("Result: You WIN!")
    elif player in [1, 2, 3]:  
        print("Result: Computer WINS!")
    else:
        print("Invalid choice! Please select 1, 2, or 3.")

def choosen():
    
    return choice([1, 2, 3])

while True:
    try:
        
        player = int(input("Enter your choice (1-Rock, 2-Paper, 3-Scissors): "))
        if player not in [1, 2, 3]:
            print("Invalid input! Please choose 1, 2, or 3.")
            continue

        
        computer = choosen()

        
        result(player, computer)

        
        play_again = input("Do you want to play again? (yes/no): ").strip().lower()
        if play_again != "yes":
            print("Thanks for playing! Goodbye!")
            break

    except ValueError:
        print("Invalid input! Please enter a number.")
