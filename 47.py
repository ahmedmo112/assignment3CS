file= open(r"textfile.txt" ,"r")

num_of_lines=0
num_of_words=0
num_of_characters=0

for line in file :
    lin =line.strip()
    word=line.split()
    num_of_words+=len(word)
    num_of_characters+=len(lin)
    num_of_lines+=1

print(f"lines => {num_of_lines}")    
print(f"characters => {num_of_characters}")   
print(f"words => {num_of_words}")   
