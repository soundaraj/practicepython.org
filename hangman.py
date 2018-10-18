import random
def game_over():
    if '-' not in list1:
        print "you win"
        return 1
    if life == 0:
        print "you loss"
        return 1   
def main():
    print("welcome to hangman")
    with open("sowpods.txt",'r') as f1:
        f2 = f1.readlines()
        guess_word = random.choice(f2)
    global life
    life = 6
    global list1
    list1 = "-" * (len(guess_word)-1)
    print list1,"tries left",'|',life,'|'
    list2 = set()
    while not game_over():
        user = raw_input("enter your guess ")
        if user.upper() in list2:
            print "already guessed"
        if len(user) <= 1:
            t = -1
            if user.upper() in guess_word:
                list2.add(user.upper())
                for i in range(2):
                    try:
                        t = guess_word.index(user.upper(),t+1)
                        list1 =list1[:t] + user.upper() + list1[t + 1:]
                    except ValueError:
                        continue
            else:
                list2.add(user.upper())
                life -= 1
                print "try again"
        else:
            print "Enter the singe character at a time"
        print list1,"tries left",'|',life,'|'
    else:
        print "the guess word is  ",guess_word
        choice = raw_input( "play again click 'Enter' else type 'q' for quit game")
        if choice == '':
            main()
        elif choice == 'q':
            print "Thank you"
            return 0
        
main()
