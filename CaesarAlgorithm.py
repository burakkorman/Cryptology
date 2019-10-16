letters = "abcçdefgğhıijklmnoöprsştuüvyz"

key = 0
enteredText = ""

def TakeKey():
    global key
    key = input("Please enter a number : ")
    while not key.isdigit():
        key = input("Incorrect entry. Please enter a number again : ")

def TakeText():
    global enteredText
    print("Enter a text : ")
    enteredText = input().lower()
    for l in enteredText:
        if((l in letters) == False):
            print("Incorrect entry. Please try again !")
            TakeText()
            break

def CryptText(key, text):
    global letters
    encrypted = ""
    for l in text :
        if(letters.index(l) + key > 28):
            encrypted += (letters[letters.index(l) + key - 29])
        else:
            encrypted += (letters[letters.index(l) + key])
    print("\n\nCRYPTED TEXT : ", encrypted, "\n\n")

def DecryptText(key, text):
    global letters
    decrypted = ""
    for l in text :
        if(letters.index(l) - key < 0):
            decrypted += (letters[letters.index(l) - key + 29])
        else:
            decrypted += (letters[letters.index(l) - key])
    print("\n\nDECRYPTED TEXT : ", decrypted, "\n\n")

while(True):
    print("1) Crypt a text")
    print("2) Decrypt a text")
    print("3) Exit")
    print("Please enter the action number : ")
    action = input()
    if(action == '1'):
        TakeKey()
        TakeText()
        CryptText(int(key),enteredText)
    if(action == '2'):
        TakeKey()
        TakeText()
        DecryptText(int(key),enteredText)
    if(action == '3'):
        break
