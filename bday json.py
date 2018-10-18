import json
dic_bday1 ={}
def add1():
     new_name = raw_input("enter the name")
     new_date = raw_input("enter the date")
     dic_bday1[new_name] = new_date
     with open("info.json",'w') as f1:
        json.dump(dic_bday1,f1)
        f1.close()
if __name__ == "__main__":
    while True:
        with open("info.json",'r') as f2:
            i = json.load(f2)
            print "\nwe know these person's bday dates  "
            for j in i:
                print j
            choice = raw_input("Who's bday date u want?")
            if choice in i:
                print choice+"'s bday is",i[choice]
            else:
                add=raw_input("this name is not in our dictionary,do u want add this name and date of birth in our dictionary,if yes type 'yes' else type 'no'")
                if add in 'yes':
                   add1()
                          
