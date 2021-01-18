
#TicTacToe
Still_playing = True

current_player = "X"

M = [".",".",".",".",".",".",".",".","."]

def Matrix():
    print(M[0] + "  | " + M[1] + " | " + M[2])
    print(M[3] + "  | " + M[4] + " | " + M[5])
    print(M[6] + "  | " + M[7] + " | " + M[8])

def players():
    print("  X or O  ")
    p1 = input("Player 1: ")
    p2 = ""
    if p1 == "X":
        p2 = "O"
        print("Player 2: " + p2)
    elif p1 == "O":
        p2 = "X"
        print("Player 2: " + p2)
    elif p1 != "O" or p1 != "X":
        print("Choose only O or X")
        play_game()

def position():
    global current_player
    print(current_player + ", it's your turn !")
    position = input("Choose a position from 1 - 9: ")
    #step5
    valid = False
    while not valid:
        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
          position = input("Choose a position from 1 - 9: ")
        position = int(position) - 1

        if M[position] == ".":
            valid = True
        else:
            print("Choose an empty position")
    M[position] = current_player
    Matrix()
#step9
def play_game():
    print("Tic Tac Toe")
    Matrix()
    players()
    #step7
    while Still_playing:
        position()
        #step8
        def winner():
            global Still_playing
            if M[0] == M[1] == M[2] != ".":
                Still_playing = False
                print(M[0]+" WON!")
            elif M[3] == M[4] == M[5] != ".":
                Still_playing = False
                print(M[3]+" WON!")
            elif M[6] == M[7] == M[8] != ".":
                Still_playing = False
                print(M[6]+" WON!")
            elif M[0] == M[3] == M[6] != ".":
                game_still_going = False
                print(M[0]+" WON!")
            elif M[1] == M[4] == M[7] != ".":
                Still_playing = False
                print(M[1]+" WON!")
            elif M[2] == M[5] == M[8] != ".":
                game_still_going = False
                print(M[2]+" WON!")
            elif M[0] == M[4] == M[8] != ".":
                Still_playing = False
                print(M[0]+" WON!")
            elif M[2] == M[4] == M[6] != ".":
                Still_playing = False
                print(M[2]+" WON!")
            elif "." not in M:
                Still_playing = False
                print("Tie")
                exit()
        
        def turn():
            global current_player
            if current_player == "X":
                current_player = "O"
            else:
                current_player = "X"
        turn()
        winner()
play_game()
