def print_board(a):
    print("",a[1]," │",a[2]," │ ",a[3]," ")
    print("────│────│────")
    print("",a[4]," │",a[5]," │ ",a[6]," ")
    print("────│────│────")
    print("",a[7]," │",a[8]," │ ",a[9]," ")


def print_instructions():
    print("\n----------- WELCOME TO TIC TAC TOE ------------\n\n")
    print_board(pos)
    print()

    players[0] = input("Enter Your Name Player 1 : ")
    players[1] = input("Enter Your Name Player 2 : ")

    print("\n-------- Instructions ---------")
    print("->", players[0], "you are using X")
    print("->", players[1], "you are using 0")
    print("-> Turn start from", players[0])
    print("-> Position are like this :-")
    print("  1 │  2 │ 3  ")
    print("────┼────┼────")
    print("  4 │ 5  │ 6  ")
    print("────┼────┼────")
    print("  7 │ 8  │ 9  ")
    print("-> press S to start the game")
    flag = input()
    return flag



def startgame():
    turn = 0
    for i in range(9):
        if turn % 2 == 0:
            print("\nThis is your turn -->", players[0])
            p = int(input("Please Enter position : "))
            v = 'x'
            pos[p] = v
            print_board(pos)
            winner = checkwin(v)
            if winner == "No one is winning the match":
                turn = 1
                continue
            else:
                print("\n\nHurray !!,", players[0], "you win the match " )
                break
        else:
            print("\nThis is your turn -->", players[1])
            p = int(input("Please Enter position : "))
            v = '0'
            pos[p] = v
            print_board(pos)
            winner = checkwin(v)
            if winner == "No one is winning the match":
                turn = 0
                continue
            else:
                print("\n\nHurray !!,", players[1], "you win the match")
                break
    else:
        print("\n\nGame is Tie")


def checkwin(v):
    for i in winning_conditions:
        if (pos[i[0]], pos[i[1]], pos[i[2]]) == (v, v, v):
            winner = players[0]
            break
        elif (pos[i[0]], pos[i[1]], pos[i[2]]) == (v, v, v):
            winner = players[1]
            break
    else:
        winner = "No one is winning the match"
    return winner



pos = ['', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
players = ['', '']
winning_conditions = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 4, 7), (2, 5, 8), (3, 6, 9), (1, 5, 9), (3, 5, 7)]
flag = print_instructions()
if flag == 's' or flag == 'S':
    startgame()
else:
    print("Invalid Entry")