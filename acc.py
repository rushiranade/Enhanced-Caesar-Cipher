# AMPLIFIED CAESAR CIPHER
def encrypt(text,s): 
    result = "" 
    n = int(input("n = "))
    for i in range(len(text)):
        char = text[i] 
        if char == " ":
            result += char
        else:
            if (char.isupper()): 
                result += chr((ord(char) + s-65) % 26 + 65) 
      
            else: 
                result += chr((ord(char) + s - 97) % 26 + 97)
        if (s * n) <=26:
            s = s * n
        else:
            s = (s - n) * n
  
    return result

def decrypt(text,s): 
    result = "" 
    n = int(input("n"))
    for i in range(len(text)):
        char = text[i] 
        if char == " ":
            result += char
        else:
            if (char.isupper()): 
                result += chr((ord(char) - s-65) % 26 + 65) 
      
            else: 
                result += chr((ord(char) - s - 97) % 26 + 97)
        if (s * n) <=26:
            s = s * n
        else:
            s = (s - n) * n
  
    return result

number = int(input("PRESS 1 TO ENCRYPT. PRESS 2 TO DECRYPT: "))
if number == 1:
    text = input("Word:")
    s = 4
    print("Cipher: " + encrypt(text,s))
elif number == 2:
    login = input("LOGIN: ")
    if encrypt(login, 4) == "EJSF": # ENCRYPTED FORM OF ABCD when n is 2. CAN BE CHANGED AS PER REQUIREMENT. 
        s = 4
        text = input("Word:")
        print("Decrypted String: " + decrypt(text,s))
    else:
        print("ACCESS DENIED")
else:
    print("PLEASE RE-RUN AND ENTER 1 OR 2")
