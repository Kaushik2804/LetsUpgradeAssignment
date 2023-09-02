import random
computer = random.choice(["Rock", "Paper", "Scissor"]).lower()
user = input("Enter your choice: 1. Rock 2. Paper 3. Scissor :  ").lower()

print("Computer choose: ", computer)
print("User choose: ", user)
print(computer, "VS", user)

if computer == user:
    print("Match tied")

elif computer == "rock" and user == "paper":
    print("You wins!!")

elif computer == "paper" and user == "scissor":
    print("You wins!!!")

elif computer == "scissor" and user == "rock":
    print("You wins!!!")

else:
    print("Computer wins!!")
