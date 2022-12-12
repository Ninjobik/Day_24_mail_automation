with open("./Input/Letters/starting_letter.txt") as letter_file:
    letter_text = letter_file.read()

with open("./Input/Names/invited_names.txt", "r") as names_file:
    names = []
    for line in names_file:
        names.append(line.strip())

save_dir = "./Output/ReadyToSend/"


def save_letter(name, ready_txt):
    with open(f"{save_dir}{name}.txt", "w") as letter:
        letter.write(ready_txt)


for name in names:
    ready_letter = letter_text.replace("[name]", name)
    save_letter(name, ready_letter)





