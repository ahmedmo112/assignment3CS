file=open(r"English.txt","r",)
dic={}

def length_of_word(file):
    for i in file:
       length_of_word=len(i.strip())
       x = i.strip('\n')
       dic[x] = length_of_word
    
length_of_word(file)

def word_length():
    for i in range(1,20):
        for key , value in dic.items():
            if value == i:
                print(key,"=>",i)

word_length()








