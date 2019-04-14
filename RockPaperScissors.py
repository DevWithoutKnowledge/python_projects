import sys
while True:
    ansplayer1=input("Player 1, do you want to play a game? Yes/No ")
    ansplayer2=input("Player 2, do you want to play a game? Yes/No ")
    agree=["yes"]
    if ansplayer1.lower() not in agree or ansplayer2.lower() not in agree:
        print("One of you didn't want to play a game! :(")
    u1=input("Choose paper/rock/scissors: ")
    u2=input("Choose paper/rock/scissors: ")
    def compare(u1, u2):
        if u1==u2:
            print("You both win!")
        elif u1!="paper" or "rock" or "scissors" or u2!="paper" or "rock" or "scissors":
            print("You chose wrong!")
            sys.exit()
        elif u1.lower()=="paper":
            if u2.lower()=="rock":
                print("Player 1 won!")
            else:
                print("Player 2 won!")
        elif u1.lower()=="rock":
            if u2.lower()=="paper":
                print("Player 2 won!")
            else:
                print("Player 1 won!")
        elif u1.lower()=="scissors":
            if u2.lower()=="paper":
                print("Player 1 won!")
            else:
                print("Player 2 won!")
        else:
            print("You made a bad decision! Try again.")
    print(compare(u1,u2))
