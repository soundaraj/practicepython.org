
def game_over():
    if '-' not in list1:
        print "you win"
        return 1
    
def main():
    print("welcome to hangman")
    guess_word = 'EVAPORATE'
    global list1
    list1 = "---------"
    print list1
    while not game_over():
        user = raw_input("enter your guess")
        if len(user) <= 1:
            t = -1
            for i in guess_word:
                if i == user.upper():
                    t = guess_word.index(i,t + 1)
                    list1 =list1[:t] + i + list1[t + 1:]
        else:
            print "Enter the singe character at a time"
        print(list1)
    else:
        choice =input( "play again enter 1")
        if choice == 1:
            main()
main()
    
   
