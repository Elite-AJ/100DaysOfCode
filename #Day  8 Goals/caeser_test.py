from art import logo
print(logo)

end_code = True
while end_code:
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))

        def caeser(text_content, shift_amount, direction_choice):
                alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
                enc_word = ""
                dec_word = ""
                if shift_amount > 25:
                        shift_amount %= 26
                        
                if direction == "encode":
                        for i in text:
                                if i not in alphabet:
                                        enc_word += i
                                else:
                                        i_location = alphabet.index(i)
                                        new_location = i_location + shift_amount
                                        if new_location > 25:
                                                amount = new_location - 26
                                                new_alpha = alphabet[amount]
                                                enc_word += new_alpha
                                        else:
                                                new_alpha = alphabet[new_location]
                                                enc_word += new_alpha
                        print(f"Here's the {direction}d result: {enc_word}")
                elif direction == "decode":
                        for i in text:
                                if i not in alphabet:
                                        dec_word += i
                                else:
                                        i_location = alphabet.index(i)
                                        new_location = i_location - shift_amount
                                        new_alpha = alphabet[new_location]
                                        dec_word += new_alpha
                        print(f"Here's the {direction}d result: {dec_word}")
        caeser(text_content = text, shift_amount = shift, direction_choice = direction)
        repeat = input("Do you want to continue? 'Yes' or 'No'\n")
        if repeat == "No":
                end_code = False
                print("Goodbye!!!")
