
def fun1():
    # read from text and print from codeC.txt
    with open("codeC.txt", "r") as file:
        for line in file:
            print(line, end="")

def fun2():
    pass

def fun3():
    pass

while True:
    print('1. Switch Case')
    print('2. Intermediate code')
    print('3. Object Code')
    print('4. Exit')

    n = int(input('Enter choice: '))
    if n == 1:
        fun1()
    elif n == 2:
        fun2()
    elif n == 3:
        fun3()
    elif n == 4:
        print('Stopped')
        break
    else:
        print('Invalid Input')