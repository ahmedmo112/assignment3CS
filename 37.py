#37
list_1=list(input("enter list 1: ").split(' '))
list_2=list(input("enter list 2: ").split(' '))


def check_the_similaritie_and_differences(list_1,list_2):
    
    for i in range(len(list_1)):
     for y in range(i+1,len(list_1)):
         if list_1[i] > list_1[y] :
            list_1 [i] ,list_1 [y] =list_1[y] ,list_1[i]
    
    for i in range(len(list_2)):
     for y in range(i+1,len(list_2)):
         if list_2[i] > list_2[y] :
            list_2 [i] ,list_2 [y] =list_2[y] ,list_2[i]     
   
    if list_1 ==list_2 :
        print("True")    
    else :
        print("False")      

check_the_similaritie_and_differences(list_1,list_2)












# x=[1,-1,3,5,6,2,7,9,8]

# for i in range(len(x)):
#      for y in range(i+1,len(x)):
#          if x[i] > x[y] :
#              x[i] , x[y] = x[y] ,x[i]
# print(x)            
            
