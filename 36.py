words = input("enter what you want to encrypt: ")

def encrypt(word):
    encryption = ''
    for char in word.lower():
        if char != " " :
            if str(char).isdecimal() or char == '.' or char==',' or char =="'" :
                encryption += char
            else:
                if char == 'z':
                    encryption +='a'
                else:    
                    encryption += chr(ord(char)+1)
    return encryption        

def decrypt(word):
    decryption = ''
    for char in word.lower():
        if char != " " : 
            if str(char).isdecimal() or char == '.' or char==',' or char =='\'':
                decryption += char   
            else:
                if char == 'a':
                    decryption += 'z'
                else:    
                    decryption += chr(ord(char)-1)
    return decryption

enc = encrypt(words)
print(enc)
dec = decrypt(enc)
print(dec)
