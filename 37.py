x= list(input("enter list 1: ").split(' '))
y= list(input("enter list 2: ").split(' '))


boollist =[]
if len(x)==len(y):
    for i in x:
        for e in y:
            if e == i:
                boollist.append('True')
            

    if len(boollist)==len(x):
        booll = True
    else :
        booll = False    
else:
    print("The Two lists are not the same")      



print(booll)