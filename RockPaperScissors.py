values = {"paper": "rock", "rock": "scissors", "scissors": "paper"}

while True:
    ansplayer1 = input("Player 1, do you want to play a game? Yes/No ")
    ansplayer2 = input("Player 2, do you want to play a game? Yes/No ")
    if ansplayer1.lower() != "yes" or ansplayer2.lower() != "yes":
        print("One of you didn't want to play a game! :(")
        exit(0)
    u1 = input("Player 1: Choose paper/rock/scissors: ")
    u2 = input("Player 2: Choose paper/rock/scissors: ")
    if u1 == u2:
        print("You both win!")
    elif values[u1] == u2:
        print("Player 1 won!")
    elif values[u2] == u1:
        print("Player 2 won!")
    else:
        print("You made a bad decision! Try again.")
