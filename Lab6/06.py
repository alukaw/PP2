import string

for letter in string.ascii_uppercase:
    with open(fr"{letter}.txt", 'w') as file:
        file.write(f"This is {letter}.txt file\n")
