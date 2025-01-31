# Description: Password Generator is a simple open-source Python program that helps users create strong, customizable passwords effortlessly.
# Developer: Jatin Kumar Mehta
# Project Version: PGB_ver.1.a
# Project Started: 29-01-2025

import random
import string

def generate_password():
    print("=== Password Generator ===")
    
    try:
        length = int(input("Enter password length: "))
        if length <= 0:
            print("Password length must be greater than zero!")
            return
    except ValueError:
        print("Invalid input! Please enter a numeric value.")
        return

    include_upper = input("Include uppercase letters? (y/n): ").strip().lower() == 'y'
    include_numbers = input("Include numbers? (y/n): ").strip().lower() == 'y'
    include_special = input("Include special characters? (y/n): ").strip().lower() == 'y'

    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    special_chars = string.punctuation

    char_pool = lowercase  # Always include lowercase letters

    if include_upper:
        char_pool += uppercase
    if include_numbers:
        char_pool += digits
    if include_special:
        char_pool += special_chars

    if not char_pool:
        print("You must select at least one character type!")
        return

    password = ''.join(random.choices(char_pool, k=length))
    print("\nGenerated Password:", password)

# Run the password generator
generate_password()