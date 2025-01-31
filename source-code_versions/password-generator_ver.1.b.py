# Description: Password Generator is a simple open-source Python program that helps users create strong, customizable passwords effortlessly.
# Developer: Jatin Kumar Mehta
# Project Version: PGB_ver.1.b
# Project Started: 30-01-2025

import random
import string

def generate_password():
    print("=== Password Generator ===")
    
    # Ask for number of passwords
    try:
        num_passwords = int(input("How many passwords do you want to generate? "))
        if num_passwords <= 0:
            print("Number of passwords must be greater than zero!")
            return
    except ValueError:
        print("Invalid input! Please enter a numeric value.")
        return
    
    # Ask for password length
    try:
        length = int(input("Enter password length: "))
        if length <= 0:
            print("Password length must be greater than zero!")
            return
    except ValueError:
        print("Invalid input! Please enter a numeric value.")
        return

    # Ask user preferences
    include_upper = input("Include uppercase letters? (y/n): ").strip().lower() == 'y'
    include_numbers = input("Include numbers? (y/n): ").strip().lower() == 'y'
    include_special = input("Include special characters? (y/n): ").strip().lower() == 'y'

    # Define character sets
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    special_chars = string.punctuation

    # Build the character pool
    char_pool = lowercase  # Always include lowercase letters
    if include_upper:
        char_pool += uppercase
    if include_numbers:
        char_pool += digits
    if include_special:
        char_pool += special_chars

    # Ensure at least one character type is selected
    if not char_pool:
        print("You must select at least one character type!")
        return

    # Generate multiple passwords
    print("\nGenerated Passwords:")
    for i in range(num_passwords):
        password = ''.join(random.choices(char_pool, k=length))
        print(f"{i + 1}. {password}")

# Run the password generator
generate_password()
