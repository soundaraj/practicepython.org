def fun1(lis1):
    list2 = list(set(list1))
    print "this list use 'set'",list2
list1 = list(input("enter"))
fun1(list1)

def fun2():
    list3 = []
    for i in list1:
        if i not in list3:
            list3.append(i)
    print "this list use 'loop'",list3
fun2()
