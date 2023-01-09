def fibonnaci(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return fibonnaci(num-1) + fibonnaci(num-2)


for i in range(int(input())):
    print(fibonnaci(i))