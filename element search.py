import random
def search(num,element):
   # print num
    for i in num:
        if i == element:
            print True
            break
        
    else:
        print False
num = list(input("enter the list"))
element = input("enter the search element")

search(num,element)

