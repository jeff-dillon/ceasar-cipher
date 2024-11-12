# add your code here
# my attempt at a caesare cipher:
###
# shift  = 15
choice =input("Type e to encrypt or d to decrypt")

if choice == 'e':
    import pjs_encryption
    pjs_encryption.encryption
elif choice == 'd':
    import pjs_decryption
    pjs_decryption.decryption
else:
    print ("wrong choice")
    