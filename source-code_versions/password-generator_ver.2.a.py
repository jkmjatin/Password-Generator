# Description: Password Generator is a simple open-source Python program that helps users create strong, customizable passwords effortlessly.
# Developer: Jatin Kumar Mehta
# Project Version: PGM_ver.2.a
# Project Started: 31-01-2025

import random
import string
import os

# File where passwords will be saved
PASSWORD_FILE = "passwords.txt"

def generate_passwords():
    print("=== Random Password Generator ===")
    
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
    passwords = []
    print("\nGenerated Passwords:")
    for i in range(num_passwords):
        password = ''.join(random.choices(char_pool, k=length))
        passwords.append(password)
        print(f"{i + 1}. {password}")

    # Let user select a password to save
    try:
        choice = int(input("\nEnter the number of the password you want to save: ")) - 1
        if 0 <= choice < num_passwords:
            selected_password = passwords[choice]
            label = input("Enter a label for this password (e.g., Instagram, Laptop, Notion): ").strip()

            # Save password to file
            with open(PASSWORD_FILE, "a") as file:
                file.write(f"{label}: {selected_password}\n")
            
            print(f"Password saved successfully under '{label}'!")
        else:
            print("Invalid selection! No password saved.")
    except ValueError:
        print("Invalid input! Please enter a valid number.")

def view_saved_passwords():
    print("\n=== Saved Passwords ===")
    
    # Check if file exists and read it
    if os.path.exists(PASSWORD_FILE):
        with open(PASSWORD_FILE, "r") as file:
            saved_passwords = file.readlines()
        
        if saved_passwords:
            for line in saved_passwords:
                print(line.strip())
        else:
            print("No passwords saved yet.")
    else:
        print("No passwords saved yet.")

def main():
    while True:
        print("\n===== Password Manager =====")
        print("1. Generate a new password")
        print("2. View saved passwords")
        print("3. Exit")
        
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            generate_passwords()
        elif choice == "2":
            view_saved_passwords()
        elif choice == "3":
            print("Exiting Password Manager. Goodbye!")
            break
        else:
            print("Invalid choice! Please enter 1, 2, or 3.")

# Run the password manager
main()