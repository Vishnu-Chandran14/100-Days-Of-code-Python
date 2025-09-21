alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

from art import logo
print(logo)

#continue the game untill user type no
should_continue = False

while not should_continue:

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: ").lower()
    text = input("Type your message: ").lower()
    shift = int(input("Type the shift number: "))

    def caesar(original_text, shift_amount, encode_or_decode):

        shifted_letter = ""


        if encode_or_decode == "decode":
            shift_amount = shift_amount * -1

        for letter in original_text:

            if letter not in alphabet:
                shifted_letter = shifted_letter + letter

            else:
                position_of_letter = alphabet.index(letter)
                new_position = position_of_letter + shift_amount
                new_position = new_position % len(alphabet)
                shifted_letter = shifted_letter + alphabet[new_position]
        print(f"Here is {encode_or_decode}d result : {shifted_letter}")


    caesar(original_text = text,shift_amount = shift, encode_or_decode= direction )

    game = input("Type 'yes' if you want to go again. Otherwise type 'no'.").lower()
    if game == 'no':
        should_continue = True
        print("Good bye")

#Create a function called encrypt() that takes original_text and shift_amount as 2 inputs.
#You need a for loop to loop through each of the letters in the plain_text.
# Find the position of each letter in the alphabet List
# Add the user desired shift_amount to the position to get the position of the encoded letter.
# Find the corresponding letter for that position.
# Add each encoded letter to a new string and print it out after the loop ends.
#
# def encrypt(original_text, shift_amount):
#     shifted_text = ""
#     for letter in original_text:
#         position_of_letter = alphabet.index(letter)
#         new_position = position_of_letter + shift_amount
#
#         #when new_position number exceeds 25, can't shift the letter, therefore get an error of out of range.
#         #we can use the modulo to get a remainder which will be within a alphabet range 0 - 25.
#
#         new_position = new_position % len(alphabet)
#         shifted_text = shifted_text + alphabet[new_position]
#     print(f"Here is the encoded result : {shifted_text}")
#
# #Call the encrypt() function and pass in the user inputs
#
# encrypt(original_text= text, shift_amount= shift)
#
# #shift each letter of the original_text forwards in the alphabet backwords by the shift amount
#
# def decrypt(original_text, shift_amount):
#     decrypt_text = ""
#     for letter in original_text:
#         position_of_letter = alphabet.index(letter)
#         new_position = position_of_letter - shift_amount
#         new_position = new_position % len(alphabet)
#         decrypt_text = decrypt_text + alphabet[new_position]
#     print(f"Here is the decoded result : {decrypt_text}")
#
# # Call the decrypt() function and pass in the user inputs
#
# decrypt(original_text=text, shift_amount=shift)
#
#
