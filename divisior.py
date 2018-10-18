'''Create a program that asks the user for a number and then prints out a list of all the divisors of that number. '''

a = int(input("enter the number"))
b = range(2,a+1)
c = []
for i in b:
    if a % i == 0:
        c.append(i)
print(c)

