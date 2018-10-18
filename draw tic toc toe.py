def horiz():
     print (" ----"* size)
def vert():
    print("|    " * (size + 1))
if __name__ == "__main__":
    size = int(input("enter"))
    for i in range(size):
        horiz()
        vert()
    
    horiz()
