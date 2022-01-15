board = {1: ' ', 2: ' ', 3: ' ',
         4: ' ', 5: ' ', 6: ' ',
         7: ' ', 8: ' ', 9: ' '}


def printBoard():
    print(board[1] + "|" + board[2] + "|" + board[3])
    print("-+-+-")
    print(board[4] + "|" + board[5] + "|" + board[6])
    print("-+-+-")
    print(board[7] + "|" + board[8] + "|" + board[9])


def game():
    if(board[1] == board[2] == board[3]):
        if(board[1] == "X"):
            print("X is Winner")
            exit()
        elif(board[1] == "O"):
            print("O is Winner")
            exit()
    elif(board[4] == board[5] == board[6]):
        if(board[4] == "X"):
            print("X is Winner")
            exit()
        elif(board[5] == "O"):
            print("O is Winner")
            exit()
    elif(board[7] == board[8] == board[9]):
        if(board[7] == "X"):
            print("X is Winner")
            exit()
        elif(board[7] == "O"):
            print("O is Winner")
            exit()
    elif(board[1] == board[4] == board[7]):
        if(board[4] == "X"):
            print("X is Winner")
            exit()
        elif(board[4] == "O"):
            print("O is Winner")
            exit()
    elif(board[2] == board[6] == board[8]):
        if(board[2] == "X"):
            print("X is Winnner")
            exit()
        elif(board[2] == "O"):
            print("O is Winner")
            exit()
    elif(board[3] == board[6] == board[9]):
        if(board[3] == "X"):
            print("X is Winner")
            exit()
        elif(board[3] == "O"):
            print("O is Winner")
            exit()
    elif(board[1] == board[5] == board[9]):
        if(board[1] == "X"):
            print("X is Winner")
            exit()
        elif(board[1] == "O"):
            print("O is Winner")
            exit()
    elif(board[3] == board[5] == board[7]):
        if(board[3] == "X"):
            print("X is Winner")
            exit()
        elif(board[3] == "O"):
            print("O is Winner")
            exit()
    elif(count == 9):
        print("Draw Match")
        exit()



count = 0

printBoard()
while True:
    count += 1
    print("X turn>>")
    x = int(input("Enter position>>"))
    while x > 9 or x < 1 or board[x] != " ":
        x = int(input("Enter the valid number>>"))

    board[x] = "X"

    printBoard()
    game()
    print("O turn>>")
    o = int(input("Enter the position>>"))

    while o > 9 or o < 1 or board[o] != " ":
        o = int(input("Enter the valid number>>"))

    board[o] = "O"
    printBoard()
    game()