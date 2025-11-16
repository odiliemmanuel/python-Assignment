player_one = str(input("Player One, select between, rock, paper,scissors: ")).lower()

player_two = str(input("Player Two, select between, rock, paper,scissors: ")).lower()

scissors = 'scissors'

paper = 'paper'

rock = 'rock'

if(player_one == scissors and player_two == rock):
    print("Player 2 wins")

if(player_one == rock and player_two == scissors):
    print("Player 1 wins")

if(player_one == scissors and player_two == paper):
    print("Player 1 wins")

if(player_one == rock and player_two == paper):
    print("Player 2 wins")

if(player_one == paper and player_two == rock):
    print("Player 1 wins")

if(player_one == paper and player_two == scissors):
    print("Player 2 wins")

if(player_one == paper and player_two == paper):
    print("Tie")

if(player_one == scissors and player_two == scissors):
    print("Tie")

if(player_one == rock and player_two == rock):
    print("Tie")

