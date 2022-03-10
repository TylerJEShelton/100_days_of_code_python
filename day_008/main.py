from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar(text_to_change, shift_text, code_direction) :
    final_text = ""
    for letter in text_to_change:
        if letter in alphabet:
            index = alphabet.index(letter)
            if code_direction == "encode":
                final_text += alphabet[index + shift_text]
            else:
                if index - shift < 0:
                    index += 26
                final_text += alphabet[index - shift_text]
        else:
            final_text += letter
    print(f"The {direction}d text is {final_text}.")


continue_cipher = True
print(logo)

while continue_cipher:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26
    caesar(text, shift, direction)
    response = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()
    if response == "no":
        continue_cipher = False
        print("Thank you for using Caesar Cipher! Goodbye!")