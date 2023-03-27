PLACEHOLDER = "[name]"
# Convert names to a list of strings
with open("./Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()
# Create a letter using starting_letter.txt
with open("./Input/Letters/starting_letter.txt") as letter_file:
    letter_contents = letter_file.read()
    # for each name in invited_names.txt
    for name in names:
        # Remove whitespace
        stripped_name = name.strip()
        # Replace the [name] placeholder with the actual name.
        new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)
        # Save the letters in the folder "ReadyToSend".
        with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.txt", "w") as completed_letter:
            completed_letter.write(new_letter)








