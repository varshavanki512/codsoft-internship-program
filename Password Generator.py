import random
import string


def generate_password(length):

    # Define the character sets for password complexity
    lowercase_chars = string.ascii_lowercase
    uppercase_chars = string.ascii_uppercase
    digits = string.digits
    special_chars = string.punctuation
    # Combine all character sets based on user's complexity preference
    all_chars = lowercase_chars + uppercase_chars + digits + special_chars
    # Check if the length is valid
    if length < 4:

        print("Password length must be at least 4 characters.")
        return None
    # Generate a password by randomly selecting characters from combined set
    password = ''.join(random.choice(all_chars) for _ in range(length))
    return password


def main():
    print("Welcome to the Password Generator")
    while True:
        try:
            length = int(input("Enter the desired password length: "))
            password = generate_password(length)
            if password:
                print("Generated Password:", password)
            another = input("Generate another password? (yes/no): ")

            if another.lower() != "yes":
                break
        except ValueError:
            print("Invalid input.Please enter a valid no. for password len.")


if __name__ == "__main__":
    main()
