# make placeholder
PLACEHOLDER = "[name]"

# Open File with names
with open("C:/Users/HP-PC/Desktop/Day 24/Mail Merge Project start/Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()
    
# Open Letter Template
with open("C:/Users/HP-PC/Desktop/Day 24/Mail Merge Project start/Input/Letters/starting_letter.txt") as letter_file:
    letter = letter_file.read()
    # Replace the placeholder with the names gotten
    for i in names:
        i = i.strip()
        new_letter = letter.replace(PLACEHOLDER, i)

        # Save each latter by the persons name using the loop function
        with open(f"C:/Users/HP-PC/Desktop/Day 24/Mail Merge Project start/Output/ReadyToSend/Letter_to_{i}.docx", mode="w") as mail_file:
            mail = mail_file.write(new_letter)

