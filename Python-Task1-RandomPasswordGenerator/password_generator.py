import random
import string

while True:
    try:
        length = int(input("Enter password length (minimum 8): "))

        if length < 8:
            print("Password length must be at least 8.")
            continue

    except ValueError:
        print("Please enter a valid number.")
        continue

    use_uppercase = input("Include uppercase letters? (y/n): ").lower()
    use_lowercase = input("Include lowercase letters? (y/n): ").lower()
    use_numbers = input("Include numbers? (y/n): ").lower()
    use_symbols = input("Include symbols? (y/n): ").lower()

    selected_types = 0

    if use_uppercase == "y":
        selected_types += 1

    if use_lowercase == "y":
        selected_types += 1

    if use_numbers == "y":
        selected_types += 1

    if use_symbols == "y":
        selected_types += 1

    if selected_types < 2:
        print("Please select at least 2 character types.")
        continue

    characters = ""

    if use_uppercase == "y":
        characters += string.ascii_uppercase

    if use_lowercase == "y":
        characters += string.ascii_lowercase

    if use_numbers == "y":
        characters += string.digits

    if use_symbols == "y":
        characters += string.punctuation

    password = ''.join(
        random.choice(characters)
        for _ in range(length)
    )

    print("Your password is:", password)

    again = input("Generate another password? (y/n): ").lower()

    if again != "y":
        print("Thank you for using the password generator!")
        break