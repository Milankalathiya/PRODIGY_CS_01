import string

alphabet = list(string.ascii_lowercase)  
alphabet_upper = list(string.ascii_uppercase) 
all_chars = list(string.printable)

def encryption(plain_message,shift):
    cipher_text = ""
    for char in plain_message:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = (position + shift) % 26
            cipher_text += alphabet[new_position]
        elif char in alphabet_upper:
            position = alphabet_upper.index(char)
            new_position = (position + shift) % 26
            cipher_text += alphabet_upper[new_position]
        elif char in all_chars:
            position = all_chars.index(char)
            new_position = (position + shift) % len(all_chars)
            cipher_text += all_chars[new_position]
        else:
            cipher_text += char
    print(f"Here's is the text after encryption: {cipher_text}")    

def decryption(encry_text,shift):
    plain_text=""
    for char in encry_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = (position - shift) % 26
            plain_text += alphabet[new_position]
        elif char in alphabet_upper:
            position = alphabet_upper.index(char)
            new_position = (position - shift) % 26
            plain_text += alphabet_upper[new_position]
        elif char in all_chars:
            position = all_chars.index(char)
            new_position = (position - shift) % len(all_chars)
            plain_text += all_chars[new_position]
        else:
            plain_text += char
    print(f"Here's is the text after dencryption: {plain_text}")    

wanna_end = False
while not wanna_end:
    what_to_do=input("Type 'encrypt' for Encryption, Type 'decrypt' for Decryption:\n")
    if what_to_do=="encrypt":
        message=input("Type your Message:\n")
        shift_key=int(input("Enter shift key:\n"))
        encryption(plain_message=message,shift=shift_key)
    elif what_to_do=="decrypt":
        message=input("Type your Message:\n")
        shift_key=int(input("Enter shift key:\n"))
        decryption(encry_text=message,shift=shift_key)
    else:
        print("Make a right choice")
    play_again = input("Type 'yes' to continue, type 'no' to exit:\n")
    if play_again=='no':
        wanna_end = True
        print("Have a nice day Bye..")