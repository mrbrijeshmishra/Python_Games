alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

def encrypt(text,shift_count):
    encoded_text = ""
    for char in text:
        shift_val = alphabet.index(char) + shift_count
        if shift_val > 25:
            shift_val -= len(alphabet)

        encoded_text += alphabet[shift_val]
    print(encoded_text)

# encrypt("qwerty",2)


def encrypt(text, shift_count):
    encoded_text = ""
    for char in text:
        shift_val = alphabet.index(char)
        new_index = (shift_val + shift_count) % len(alphabet)
        encoded_text += alphabet[new_index]
    print(encoded_text)

encrypt("qwerty", 2)




def decrypt(text,shift_count):
    encoded_text = ""
    for char in text:
        shift_val = alphabet.index(char) - shift_count
        if shift_val < 0:
            shift_val += len(alphabet)

        encoded_text += alphabet[shift_val]
    print(encoded_text)

# decrypt("sygtva",2)


def decrypt(text, shift_count):
    encoded_text = ""
    for char in text:
        shift_val = alphabet.index(char)
        new_index = (shift_val - shift_count) % 26
        encoded_text += alphabet[new_index]
    print(encoded_text)

# decrypt("sygtva", 2)

print("Enter encrypt to Encrypt value or decrypt to Decrypt value")

user_selection = input("Please provide an option to move further:").lower()
if user_selection == 'encrypt':
    text = input("Enter the text to encode:")
    shift_count = input("Enter the count to shift value:")
    encrypt(text,shift_count)
elif user_selection == 'decrypt':
    text = input("Enter the text to decode:")
    shift_count = input("Enter the count to shift value:")
    decrypt(text,shift_count)
else:
    print("Invalid selection, sorry try again later!!!!!!!!!!")