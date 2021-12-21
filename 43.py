number = [1,2,3,4,5,6,7,8,9]
p1 = []
p2 = []

def checkthesumofthree(p):
    if len(p)==4:
        if p[0]+p[1]+p[2]==15 or p[0]+p[1]+p[3]==15 or p[3]+p[1]+p[2]==15 or p[0]+p[2]+p[3]==15:
            return True 
    elif len(p)==3:
        if p[0]+p[1]+p[2]==15:
            return True

def checkwin():
    if len(p1) ==4 and len(p2) == 4 and checkthesumofthree(p1) == checkthesumofthree(p2):
        print("drew")
        exit()
    elif checkthesumofthree(p1):
        print("player 1 wins")
        exit()
    elif checkthesumofthree(p2) and len(p2)>2:
        print("player 2 wins")
        exit()

def game():
    while len(number) > 1:
        x = int(input(f"palyer 1 choose number from {number}: "))
        while x not in number:
            print("this number is not in the numbers")
            x = int(input(f"palyer 1 choose number from {number}: "))
            
        p1.append(x)
        number.remove(x)
        if len(p1)==3:
            checkwin()
        x = int(input(f"player 2 choose number from {number}: "))
        while x not in number:
            print("this number is not in the numbers")
            x = int(input(f"palyer 2 choose number from {number}: "))
        p2.append(x)
        number.remove(x)
        if len(p2)==3:
            checkwin()

game()

checkwin()
