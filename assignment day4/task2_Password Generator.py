
# Assignment 4 - Task 2: Password Generator

import random


letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
    'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
    'u', 'v', 'w', 'x', 'y', 'z',
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
    'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
    'U', 'V', 'W', 'X', 'Y', 'Z'
]

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']



def generate_password(num_letters, num_symbols, num_numbers):

    password_characters = []

    
    for _ in range(num_letters):
        password_characters.append(random.choice(letters))

    
    for _ in range(num_symbols):
        password_characters.append(random.choice(symbols))

    
    for _ in range(num_numbers):
        password_characters.append(random.choice(numbers))

    
    random.shuffle(password_characters)

    
    password = ''.join(password_characters)

    return password



def main():
    print("========== PASSWORD GENERATOR ==========")

    num_letters = int(
        input("How many letters would you like in your password? ")
    )

    num_symbols = int(
        input("How many symbols would you like? ")
    )

    num_numbers = int(
        input("How many numbers would you like? ")
    )

    
    if min(num_letters, num_symbols, num_numbers) < 0:
        print("Please enter non-negative numbers.")
        return

    if num_letters + num_symbols + num_numbers == 0:
        print("Password length must be greater than zero.")
        return

    # Generate password
    password = generate_password(
        num_letters, num_symbols, num_numbers
    )

    print("\n========== PASSWORD SUMMARY ==========")
    print(f"Letters requested: {num_letters}")
    print(f"Symbols requested: {num_symbols}")
    print(f"Numbers requested: {num_numbers}")
    print(f"Total password length: {len(password)}")
    print(f"Generated password: {password}")


if __name__ == "__main__":
    main()
