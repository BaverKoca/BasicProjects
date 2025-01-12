import random
import string

def generate_password(length=12, uppercase=True, lowercase=True, digits=True, special_chars=True):
    characters = ""

    if uppercase:
        characters += string.ascii_uppercase
    if lowercase:
        characters += string.ascii_lowercase
    if digits:
        characters += string.digits
    if special_chars:
        characters += string.punctuation

    if not any([uppercase, lowercase, digits, special_chars]):
        print("At least one of the parameters uppercase, lowercase, digits, special_chars must be True.")

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Password Generator")
    length = int(input("Enter length of password: "))
    uppercase = input("Include capital letters? (Y/N): ").upper() == 'Y'
    lowercase = input("Do you include lowercase letters? (Y/N): ").upper() == 'Y'
    digits = input("Do you want to include numbers? (Y/N): ").upper() == 'Y'
    special_chars = input("Include special characters? (Y/N): ").upper() == 'Y'

    password = generate_password(length, uppercase, lowercase, digits, special_chars)
    print("Created Password:", password)

if __name__ == "__main__":
    main()
