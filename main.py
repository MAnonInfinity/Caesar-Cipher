import art

print(art.logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesarCipher(text, shift, direction):
    if direction == 'd': #decode
        shift = shift *(-1)
    if shift > 25: #manage large shifts/keys
        shift %= 26
        
    finalText=""
    
    for i in text: #process the cipher
        if i == ' ' or i.isdigit():
            finalText += i
            continue
        indexx = alphabet.index(i)
        finalText += alphabet[(indexx + shift) % 26]

    if direction == 'd':
        print(f"\nThe decoded text = {finalText}")
    elif direction == 'e':
        print(f"\nThe encoded text = {finalText}")
    else:
        print("Invalid Choice")

while True:
    yesOrNo = input("\nType 'y' if you want to go in, otherwise type 'n'\n").lower()
    if yesOrNo == 'n':
        print("Goodbye")
        break
    direction = input("Type 'e' to encrypt, type 'd' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number (key) :\n"))
    caesarCipher(text, shift, direction)


