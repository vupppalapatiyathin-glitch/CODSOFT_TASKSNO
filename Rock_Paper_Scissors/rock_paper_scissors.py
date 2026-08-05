#rock_paper_scissors in python 

import random
user_score = 0
computer_score = 0
choices = ["rock", "paper", "scissors"]
while True:
    user = input("Enter rock, paper, or scissors: ").lower()
    if user not in choices:
        print("Invalid choice! Please try again.\n")
        continue
    computer = random.choice(choices)
    print("You chose:", user)
    print("Computer chose:", computer)
    if user == computer:
        print("It's a Tie!")
    elif (user == "rock" and computer == "scissors") or \
         (user == "paper" and computer == "rock") or \
         (user == "scissors" and computer == "paper"):
        print("You Win!")
        user_score += 1
    else:
        print("Computer Wins!")
        computer_score += 1
    print("\nScore:")
    print("You:", user_score)
    print("Computer:", computer_score)
    play_again = input("\nDo you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        print("\nFinal Score")
        print("You:", user_score)
        print("Computer:", computer_score)
        print("Thank you for playing!")
        break
print()