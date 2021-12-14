x=list(input("enter a list : ").split(' '))

def check_the_arangment(x):
    if x == sorted(x):   #Ascending
        return '1'
    elif x == sorted(x,reverse=True):  #Descending
        return '-1'
    else:
        return '0'
print(check_the_arangment(x))



 






