def restart():
    global game
    game =[['.']*3 for game in range(3)]
    main()
def p1(p,piece):
    print ("player"+str(p)+":")
    value = raw_input("enter the range")
    r = value.split(',')
    row = int(r[0])-1
    col = int(r[1])-1
    if p == 1:
        if game[row][col] == '.':
            game[row][col] = piece 
        else:
            print "try again"
    else:
        if game[row][col] == '.':
            game[row][col] = piece 
        else:
            print "try again"
        
    for i in range(0,3):
        print(" ---"*3)
        print("| "+game[i][0]+" | "+game[i][1]+" | "+game[i][2]+" |")
    print(" ---"*3)  
def game_over():
    searcht = '.'
    
    # check win by row
    for i in range(3):
        if len(set(game[i])) == 1:
            if game[i][1] == '.':
                continue
            elif game[i][1] == 'X':
                print ("Game over - Player 1 wins")
                return 1
            #elif gameboard[i][1] == 'O':
            else:
                print ("Game over - Player 2 wins")
                return 1
            return 1

    # check win by column
    for i in range(3):
        if game[0][i] == game[1][i] == game[2][i]:
            if game[0][i] == '.':
                continue
            elif game[0][i] == 'X':
                print ("Game over - Player 1 wins")
                return 1
            else:
                print( "Game over - Player 2 wins")
                return 1
            return 1

    # check win by diagonal
    if (game[0][0] == game[1][1] == game[2][2]) or (game[0][2] == game[1][1] == game[2][0]): 
        if game[1][1] == 'X':
            print( "Game over - Player 1 wins")
            return 1
        elif game[1][1] == 'O':
            print( "Game over - Player 2 wins")
            return 1
        else:
            return 0
        return 1

    # check board is full
    for sublist in game:
        if searcht in sublist:
            return 0

    print( "Game over - the board is filled")
    return 1
def main():
     p = 1
     turn = 1
     piece = '.'
     while not game_over():
         player = turn % 2
         if player == 0:
            p = 2
            piece = 'O'
            p1(p,piece)
         else:
            p = 1
            piece = 'X'
            p1(p,piece)
         
         turn += 1
     else:
         chance=int(input('play again enter 1'))
         if chance == 1:
            restart()
if __name__ == "__main__":
    restart()   
