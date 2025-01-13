#Rock Paper Scissors

#init
import random
wins = 0
losses = 0
ties = 0

#Function
def RockPaperScissors():
    global wins
    global losses
    global ties
    print("Welcome to Rock Paper Scissors!")
    while True:
        #Step 1: Collect player's move
        print("Make your move!")
        player = input("Rock, Paper, Scissors, Shoot: ")

        #Step 2: Generate a move for the computer

        computer = random.randint(1,3)
        if computer  == 1:
            computer = "Rock"
            print("The computer's move is Rock!")
        elif computer == 2:
            computer = "Paper"
            print("The computer's move is Paper!")
        elif computer == 3:
            computer = "Scissors"
            print("The computer's move is Scissors!")

    #Step 3: Determine the Outcome
        if player.capitalize() == "Rock" and computer == "Rock":
            print ("It's a tie!")
            ties = ties + 1
        elif player.capitalize() == "Rock" and computer == "Paper":
            print("You were defeated by the computer!")
            losses = losses + 1
        elif player.capitalize() == "Rock" and computer == "Scissors":
            print("You beat the computer!")
            wins = wins + 1
        elif player.capitalize() == "Paper" and computer == "Rock":
            print("You beat the computer!")
            wins = wins + 1
        elif player.capitalize() == "Paper" and computer == "Paper":
            print("It's a tie!")
            ties = ties + 1
        elif player.capitalize() == "Paper" and computer == "Scissors":
            print("You were defeated by the computer!")
            losses = losses + 1
        elif player.capitalize() == "Scissors" and computer == "Rock":
            print("You were defeated by the computer!")
            losses = losses + 1
        elif player.capitalize() == "Scissors" and computer == "Paper":
            print("You beat the computer!")
            wins = wins + 1
        elif player.capitalize() == "Scissors" and computer == "Scissors":
            print("It's a tie!")
            ties = ties + 1

        #Step 4: Loop the program until player wants to quit
        PlayAgain = input("Here is your record so far. You have " + str(wins) + " win(s), " + str(losses) + " loss(es), and " + str(ties) + " tie(s). Player: " + str(wins) + " / Computer: " + str(losses) + ". Would you like to play again? (Y, N)_: ")
        if PlayAgain.upper() == "Y": 
            print("Restarting...")
        else:
            print("Thanks for playing!")
            break

        #Step 5: Keep track of wins and losses

#Main
RockPaperScissors()




