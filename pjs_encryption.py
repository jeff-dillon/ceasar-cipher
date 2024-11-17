#my module for encryption

import string

def encryption():
   
    import string 
plain_text = input("what do you want to encrypt? ")
shift  = int(input("Please enter encrytion key. "))
alphabet = string.ascii_lowercase
shifted = alphabet[shift:] + alphabet[:shift]
table = str.maketrans(alphabet, shifted)

encrypted = plain_text.translate(table)

print(encrypted)