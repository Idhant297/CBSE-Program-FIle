def push(stack, item):
    stack.append(item)
    print("Item pushed to stack")


def pop(stack):
    if len(stack) == 0:
        print("Stack is empty")
    else:
        stack.pop()
        print("Item popped from stack")


def peek(stack):
    if len(stack) == 0:
        print("Stack is empty")
    else:
        print(stack[-1])


def display(stack):
    if len(stack) == 0:
        print("Stack is empty")
    else:
        print(stack)


def main():
    stack = []
    choice = 0
    while choice != 6:
        print("1. Push")
        print("2. Pop")
        print("3. Peek")
        print("4. Display")
        print("5. Exit")
        choice = int(input("Enter your choice : "))
        if choice == 1:
            item = input("Enter the item to be pushed : ")
            push(stack, item)
        elif choice == 2:
            pop(stack)
        elif choice == 3:
            peek(stack)
        elif choice == 4:
            display(stack)
        elif choice == 5:
            exit()
        else:
            print("Wrong choice")


if __name__ == '__main__':
    main()