import random

l = ["rock", "scissor", "paper"]

while True:
    uc = int(input('''
Game Start......
1 Yes
2 No | Exit
: '''))

    if uc == 1:
        for a in range(1, 6):   # 5 rounds
            print("\nRound", a)

            userInput = int(input('''
1 Rock
2 Scissor
3 Paper
: '''))

            if userInput == 1:
                uchoice = "rock"
            elif userInput == 2:
                uchoice = "scissor"
            elif userInput == 3:
                uchoice = "paper"
            else:
                print("Invalid choice")
                continue

            
            Cchoice = random.choice(l)

            print("Your choice:", uchoice)
            print("Computer choice:", Cchoice)

            
            if Cchoice == uchoice:
                print("Result: It's a Tie")
            elif (uchoice == "rock" and Cchoice == "scissor") or \
                 (uchoice == "scissor" and Cchoice == "paper") or \
                 (uchoice == "paper" and Cchoice == "rock"):
                print("Result: You Win")
            else:
                print("Result: Computer Wins")

    elif uc == 2:
        print("Game Exited")
        break
    else:
        print("Invalid option")