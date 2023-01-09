import pickle

def write():
    f=open("student.dat","ab")
    name=input("Enter the name of student: ")
    rollno=int(input("Enter the roll no of student: "))
    marks=int(input("Enter the marks of student: "))
    s=[name,rollno,marks]
    pickle.dump(s,f)
    f.close()

def read():
    f=open("student.dat","rb")
    try:
        while True:
            s=pickle.load(f)
            print("Name:",s[0])
            print("Roll no:",s[1])
            print("Marks:",s[2])
            print()
    except EOFError:
        f.close()

def search():
    f=open("student.dat","rb")
    rollno=int(input("Enter the roll no to be searched: "))
    try:
        while True:
            s=pickle.load(f)
            if s[1]==rollno:
                print("Name:",s[0])
                print("Rollno:",s[1])
                print("Marks:",s[2])
                print()
            
    except EOFError:
        f.close()

print('1.Enter Data\n2.Read Data\n3.Search Data\n4.Exit')
lol=False
while not lol:
    choice=int(input("Enter Choice: "))
    if choice==1:
        write()
    elif choice==2:
        read()
    elif choice==3:
        search()
    elif choice==4:
        lol=True
    else:
        print('Invalid Choice')