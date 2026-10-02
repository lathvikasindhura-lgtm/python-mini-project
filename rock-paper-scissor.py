
import random

print("Welcome to Rock, Paper, Scissors Game!")

choices = ["rock", "paper", "scissors"]

user = input("Enter your choice (rock/paper/scissors): ").lower()

computer = random.choice(choices)

print("You chose:", user)
print("Computer chose:", computer)

if user not in choices:
    print("Invalid choice! Please enter rock, paper, or scissors.")

elif user == computer:
    print("It's a Tie!")

elif user == "rock" and computer == "scissors":
    print("You Win!")

elif user == "paper" and computer == "rock":
    print("You Win!")

elif user == "scissors" and computer == "paper":
    print("You Win!")

else:
    print("Computer Wins!")

print("Thank you for playing!")