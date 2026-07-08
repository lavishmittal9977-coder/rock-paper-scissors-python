import random
choice=["rock","paper","scissor"]
user_score=0
computer_score=0
print("-----Rock Paper Scissor Game-----")
print("Type 'exit' anytime to quit  the game.\n ")
for i in range(5):
    print(f"Round{i+1}")
    computer=random.choice(choice)
    user=input("Enter the  your choice:")
    print("computer choice:",computer)
    if user=="exit":
        print("Game ended!")
        break
    if user not in choice:
        print("invalid choice!")
        continue
    if user==computer:
        print("match draw")
    elif (user=="rock" and computer=="scissor") or (user=="paper" and computer=="rock") or (user=="scissor" and computer=="paper"):
        print("You won This Round")
        user_score+=1
    else:
        print("computer won This Round")
        computer_score+=1
    print("Your Score:",user_score)
    print("Computer Score:",computer_score)
    print("-"*30)
print("\n------Final Result------")
print("Your Score:",user_score)
print("Computer Score:",computer_score)
if user_score> computer_score:
    print("🎉Congratulations!you won the match")
elif computer_score>user_score:
    print("😔 Computer Won the match.")
else:
    print("🤝 Match Draw!")