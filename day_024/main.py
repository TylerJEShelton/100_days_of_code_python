# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

names_list = []

with open("./Input/Letters/starting_letter.txt") as file:
    starting_letter = file.read()

with open("./Input/Names/invited_names.txt", "r") as file:
    for line in file:
        names_list.append(line[0:-1])

for name in names_list:
    edited_letter = starting_letter.replace("[name]", f"{name}")
    with open(f"./Output/ReadyToSend/letter_for_{name}.txt", "w") as file:
        file.write(edited_letter)