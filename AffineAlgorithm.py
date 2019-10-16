letters = "abcçdefgğhıijklmnoöprsştuüvyz"

a = 0
b = 0
enteredText = ""

def TakeKeys():
    global a,b
    a = input("Please enter the a variable : ")
    while not a.isdigit():
        a = input("Incorrect entry. Please enter the a variable : ")

    b = input("Please enter the b variable : ")
    while not a.isdigit():
        a = input("Incorrect entry. Please enter the b variable : ")

def TakeText():
    global enteredText
    enteredText = input("Enter a text : ")
    for l in enteredText:
        if((l in letters) == False):
            print("Incorrect entry. Please enter a text : ")
            TakeText()
            break

def FindZValue(a):
    for i in range(len(letters)):
        if( (a * i) % len(letters) == 1):
            return i

def CryptText(a,b,text):
    global letters
    encrypted = ""
    for l in text :
        cryptedLetterIndex = (a * letters.index(l) + b)
        if(cryptedLetterIndex >= 29):
            cryptedLetterIndex = cryptedLetterIndex % len(letters)
        encrypted += letters[cryptedLetterIndex]
    print("\n\nCRYPTED TEXT : ", encrypted, "\n\n")

def DecryptText(a,b,text):
    global letters
    decrypted = ""
    for l in text : 
        z = FindZValue(a)
        decrypted += letters[(z * (letters.index(l) - b)) % len(letters)]
    print("\n\nDECRYPTED TEXT : ", decrypted, "\n\n")

while(True):
    print("1) Crypt a text")
    print("2) Decrypt a text")
    print("3) Exit")
    print("Please enter the action number : ")
    action = input()
    if(action == '1'):
        TakeKeys()
        TakeText()
        CryptText(int(a),int(b),enteredText)
    if(action == '2'):
        TakeKeys()
        TakeText()
        DecryptText(int(a),int(b),enteredText)
    if(action == '3'):
        break