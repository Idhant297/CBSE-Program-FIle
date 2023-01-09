import csv

def write_data():
    f_obj = open('Data.csv', 'a', newline='')
    w_obj = csv.writer(f_obj)
    n = input('Enter name: ')
    mb = input('Enter mobile number: ')
    addr = input('Enter address: ')
    rec = [n, mb, addr]
    w_obj.writerow(rec)
    f_obj.close()


def read_data():
    f_obj = open('Data.csv', 'r')
    r_obj = csv.reader(f_obj)
    for r in r_obj:
        print(r)
    f_obj.close()


def search_data():
    f_obj = open('Data.csv', 'r')
    r_obj = csv.reader(f_obj)
    n = input('Enter name: ')
    for i in r_obj:
        if n == i[0]:
            print(i)

    f_obj.close()


print('1.Enter Data\n2.Read Data\n3.Search Data\n4.Exit')
check = False
while not check:
    choice = int(input("Enter Choice: "))
    if choice == 1:
        write_data()
    elif choice == 2:
        read_data()
    elif choice == 3:
        search_data()
    elif choice == 4:
        print("Program Closed.")
        check = True
    else:
        print('Invalid Choice')