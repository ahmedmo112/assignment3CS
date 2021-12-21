firstfile = open("first-file.txt", "w")
firstfile.write("Hello World\nCS111\nI LOVE PYTHON")
firstfile.close() # gentrate file

firstfile = open("first-file.txt", "r") #read from file
secondfile = open("second-file.txt", "w") #write in file

for line in firstfile:
    secondfile.write(line)

firstfile.close()
secondfile.close()