#decypt

import string

def decryption():
   
    import string 
plain_text = input("what do you want to decrypt? ")
shift1  = int(input("Please enter decrytion key ")) 
shift = 26-shift1
alphabet = string.ascii_lowercase
shifted = alphabet[shift:] + alphabet[:shift]
table = str.maketrans(alphabet, shifted)
decrypted = plain_text.translate(table)
print(decrypted)