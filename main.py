import random
import string

def generate_password(min_length, numbers=True, special_characters=True):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation

    characters = letters
    if numbers:
        characters += digits
    if special_characters:
        characters += special

    pwd = ""
    meets_criteria = False
    has_number = False
    has_special = False

    while not meets_criteria or len(pwd) < min_length:
        new_char = random.choice(characters)
        pwd += new_char

        if new_char in digits:
            has_number = True
        elif new_char in special:
            has_special = True

        meets_criteria = True
        if numbers:
            meets_criteria = has_number
        if special_characters:
            meets_criteria = meets_criteria and has_special

    return pwd

def get_length():
    while True:
        try:
            length = int(input("Enter the minimum length you want your password: "))
            if length <= 7:
                print("A secure password is 8 or more characters.\n")
                continue
            return length
        except ValueError:
            print("Please enter a number.\n")

def main():
    print("Welcome to my password generator!")
    length = get_length()
    pwd = generate_password(length)
    print(f"Your password is: {pwd}")

if __name__ == "__main__":
    main()