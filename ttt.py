# TIC-TAC-TOE

def reset():
    return {1 : " ", 2 : " ", 3 : " ",
         4 : " ", 5 : " ", 6 : " ",
         7 : " ", 8 : " ", 9 : " "}

board = reset()

def printBoard(board):
    print(board[1] + "|" + board[2] + "|" + board[3])
    print("-+-+-")
    print(board[4] + "|" + board[5] + "|" + board[6])
    print("-+-+-")
    print(board[7] + "|" + board[8] + "|" + board[9])

def game(board):
    count = 1
    printBoard(board)
    while True:
        print("1.Top-Left\n2.Top-Center\n3.Top-Right\n4.Center-Left\n5.Center-Center\n6.Center-Right\n7.Bottom-Left\n8.Bottom-Center\n9.Bottom-Right\n")
        if count%2 == 1 :
            turn = "X"
        elif count%2 == 0:
            turn = "O"

        print(turn + "'s turn>> ")
        move = int(input())

        while(board[move] != " "):
            print("Invalid input")
            print("Give a valid input>>")
            move = int(input())

        board[move] = turn
        printBoard(board)

        if(count>5):
            if(board[1] == board[2] == board[3] == turn):
                print(turn + " WON")
                break
            if(board[4] == board[5] == board[6] == turn):
                print(turn + " WON")
                break
            if(board[7] == board[8] == board[9] == turn):
                print(turn + " WON")
                break
            if(board[1] == board[4] == board[7] == turn):
                print(turn + " WON")
                break
            if(board[2] == board[6] == board[8] == turn):
                print(turn + " WON")
                break
            if(board[3] == board[6] == board[9] == turn):
                print(turn + " WON")
                break
            if(board[1] == board[5] == board[9] == turn):
                print(turn + " WON")
                break
            if(board[3] == board[5] == board[7] == turn):
                print(turn + " WON")
                break
        count = count + 1

print("Let's Play TIC-TAC-TOE>>")
game(board)

while True:
    print("Want to play new game? (1.Yes\n2.No)")
    again = int(input())

    if again == 1:
        board = reset()
        game(board)

    if again == 2:
        exit()