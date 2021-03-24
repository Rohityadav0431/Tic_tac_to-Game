board =['' for x in range(10)]

def insert_letter(letter,pos):
    board[pos]=letter
    
def free_space(pos):
    return board[pos]==" "

def print_board(board):
    print("   |   |   ")
    print(" " + board[1] + " | " + board[2] + " | " + board[3])
    print("   |   |   ")
    print("------------")
    print("   |   |   ")
    print(" " + board[4] + " | " + board[5] + " | " + board[6])
    print("   |   |   ")
    print("------------")
    print("   |   |   ")
    print(" " + board[7] + " | " + board[8] + " | " + board[9])
    print("   |   |   ")
def nospace(board):
    if board.count(' ') > 1: #this function is checking that board is full or not that's means if there is  boxes is free that's mean value of empty string is greaterthan 1 then board is free and return false
        return False
    else:
        return True
def winner(b,l):
    return (b[1])==l and (b[2])==l and (b[3])==l or (b[1])==l and (b[4])==l and (b[7])==l or (b[1])==l and (b[5])==l and (b[9])==l or (b[4])==l and (b[5])==l and (b[6])==l or (b[7])==l and (b[8])==l and (b[9])==l or (b[2])==l and (b[5])==l and (b[8])==l or (b[3])==l and (b[6])==l and (b[9])==l or (b[3])==l and (b[5])==l and (b[7])==l
    
     
def player_move():
    run = True
    while run:
        move =input("please select a position to enter x between 1 to 9")
        try:
            move = int(move)
            if move > 0 and move < 10:
                if free_space(move):
                    run = False
                    insert_letter('x',move)
                else:
                    print("sorry this space is occupied")
            else:
                print("type number between 1 and 9")
        except:
            print("type a number")
            
def computer_move():
    possible_moves = [x for x, letter in enumerate(board) if letter == ' ' and x !=0 ]
    move =0
    for let in ['o','x']:
        for i in possible_moves:
            boardcopy=board[:]
            boardcopy[i]=let
            if winner(boardcopy,let):
                move = i
                return move
    corners=[]
    for i in possible_moves:
        if i in [1,3,7,9]:
            corners.append(i)
    if len(corners) > 0:
        move = select_random(corners)
        return move
    if 5 in possible_moves:
        move=5
        return move
    edges=[]
    for i in possible_move:
        if i in [2,4,6,8]:
            edges.append(i)
    
    if len(edges) >0:
        move = select_random(edges)
        return move
def select_random(li):
    import random
    ln=len(li)
    r=random.randrange(0,ln)
    return li[r]
def main():
    print("welcome to game")
    print_board(board)
    
    while not(nospace(board)):
        if not(winner(board,'o')):
            player_move()
            print_board(board)
        else:
            print("sorry you loose")
            break
        if not(winner(board,'x')):
            move=computer_move()
            if move==0:
                print("tie game")
            else:
                insert_letter('o',move)
                print("computer placed an o in position",move,":")
                print_board(board)
        else:
            print("you win")
            break
                
    if nospace(board):
        print('tie game')

while True:
    x=input("do you want to play again (y/n)")
    if x.lower()=="y":
        board=[' ' for x in range(10)]
        print("-------------------")
        main()
    else:
        break
