letters = "abcçdefgğhıijklmnoöprsştuüvyz"
shuffle = "eğilortvaçfhjmösuybdgıknpşüzc"

enteredText = ""

def TakeText():
    global enteredText
    enteredText = input("Enter a text : ")
    for l in enteredText:
        if((l in letters) == False):
            print("Incorrect entry. Please enter a text : ")
            TakeText()
            break


def CryptText(text):
    encrypted = ""
    for l in text :
        encrypted += shuffle[letters.index(l)]
    print("\n\nCRYPTED TEXT : ", encrypted, "\n\n")

def DecryptText(text):
    decrypted = ""
    for l in text : 
        decrypted += letters[shuffle.index(l)]
    print("\n\nDECRYPTED TEXT : ", decrypted, "\n\n")

while(True):
    print("1) Crypt a text")
    print("2) Decrypt a text")
    print("3) Exit")
    print("Please enter the action number : ")
    action = input()
    if(action == '1'):
        TakeText()
        CryptText(enteredText)
    if(action == '2'):
        TakeText()
        DecryptText(enteredText)
    if(action == '3'):
        break