# Caesar Cipher

def encrypt(og,sh):
    new_text = ""
    shift  = None
    for i in og:
        shift = ord(i)+ sh
        if shift > 122:
            new_text += chr(shift-26)
        else:
            new_text += chr(shift)
    print(f"Here is the encoded result: {new_text}")
def decrypt(og,sh):
    new_text = ""
    shift = None
    for i in og:
        shift = (ord(i) - sh)
        if shift < 97:
            new_text += chr(shift+26)
        else:
            new_text += chr(shift)
    print(f"Here is the decoded result: {new_text}")


direction = input("Type 'encode' to encrypt the message or Type 'decode' to decrypt the message:\n").casefold()
original_text = input("Enter the text:\n").casefold()
shift_amount = int(input("Enter the shift:\n"))
shift_amount = (shift_amount)%26
if direction == "encode":
    encrypt(original_text, shift_amount)
elif direction == "decode":
    decrypt(original_text, shift_amount)
else:
    print("Invalid choice. Please type 'encode' or 'decode'.")

