import string


def decryption():
   
    import string 
plain_text = input("what do you want to decrypt? ")
shift  = -int(input-26("Please enter decrytion key"))
alphabet = string.ascii_lowercase
shifted = alphabet[shift:] + alphabet[:shift]
table = str.maketrans(alphabet, shifted)
decrypted = plain_text.translate(table)
print(decrypted)