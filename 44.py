from math import sqrt


coins = int(input("Coins number: "))

while coins > 0:
    z = int(sqrt(coins))
    print(f"The range from 1 to {z}")
    p1 = int(input("Player 1:"))
    while p1 > z or p1<0:
        p1 = int(input("Player 1 input wrong number enter number between the range: "))
        
    coins -= (p1*p1)
    print(f"coins number {coins}")
    z = int(sqrt(coins))
    if z == 0:
        print("Player 1 win")
        break
    print(f"the range from 1 to {z}")
    p2 = int(input("Player 2:"))
    while p2 > z or p2<0:
        p2 = int(input("player 2 input wrong number enter number between the range:"))
    coins -= (p2*p2)
    print(f"coins number {coins}")
    z = int(sqrt(coins))
    if z == 0:
        print("Player 2 win")
        break