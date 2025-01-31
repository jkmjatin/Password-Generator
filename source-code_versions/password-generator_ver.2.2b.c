#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
#include <time.h>

#define PASSWORD_FILE "passwords.txt"
#define MAX_PASSWORDS 100
#define MAX_LENGTH 100

// Function to calculate password strength
int calculate_password_strength(const char *password) {
    int score = 0, length = strlen(password);
    int has_lower = 0, has_upper = 0, has_digit = 0, has_special = 0;
    
    if (length >= 8) score += 2;
    if (length >= 12) score += 2;
    
    for (int i = 0; i < length; i++) {
        if (islower(password[i])) has_lower = 1;
        if (isupper(password[i])) has_upper = 1;
        if (isdigit(password[i])) has_digit = 1;
        if (strchr("!@#$%^&*()-_=+[]{}|;:,.<>?/", password[i])) has_special = 1;
    }
    
    score += (has_lower + has_upper) * 2 + has_digit + has_special;
    return score > 10 ? 10 : score;
}

// Function to generate a password
void generate_password(char *password, int length, int include_upper, int include_numbers, int include_special) {
    const char *lowercase = "abcdefghijklmnopqrstuvwxyz";
    const char *uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    const char *digits = "0123456789";
    const char *special_chars = "!@#$%^&*()-_=+[]{}|;:,.<>?/";
    
    char char_pool[MAX_LENGTH] = "";
    strcat(char_pool, lowercase);
    if (include_upper) strcat(char_pool, uppercase);
    if (include_numbers) strcat(char_pool, digits);
    if (include_special) strcat(char_pool, special_chars);
    
    int pool_size = strlen(char_pool);
    for (int i = 0; i < length; i++) {
        password[i] = char_pool[rand() % pool_size];
    }
    password[length] = '\0';
}

// Function to save password
void save_password(const char *label, const char *password) {
    FILE *file = fopen(PASSWORD_FILE, "a");
    if (file == NULL) {
        printf("Error opening file!\n");
        return;
    }
    fprintf(file, "%s: %s\n", label, password);
    fclose(file);
    printf("Password saved successfully under '%s'!\n", label);
}

// Function to view saved passwords
void view_saved_passwords() {
    FILE *file = fopen(PASSWORD_FILE, "r");
    if (file == NULL) {
        printf("No passwords saved yet.\n");
        return;
    }
    
    char line[MAX_LENGTH];
    printf("\n=== Saved Passwords ===\n");
    while (fgets(line, sizeof(line), file)) {
        printf("%s", line);
    }
    fclose(file);
}

// Function to delete a saved password
void delete_saved_password() {
    FILE *file = fopen(PASSWORD_FILE, "r");
    if (file == NULL) {
        printf("No saved passwords found.\n");
        return;
    }
    
    char lines[MAX_PASSWORDS][MAX_LENGTH];
    int count = 0;
    while (fgets(lines[count], MAX_LENGTH, file) && count < MAX_PASSWORDS) {
        count++;
    }
    fclose(file);
    
    if (count == 0) {
        printf("No passwords to delete.\n");
        return;
    }
    
    for (int i = 0; i < count; i++) {
        printf("%d. %s", i + 1, lines[i]);
    }
    
    int choice;
    printf("Enter the number of the password to delete: ");
    scanf("%d", &choice);
    getchar();
    
    if (choice < 1 || choice > count) {
        printf("Invalid selection!\n");
        return;
    }
    
    file = fopen(PASSWORD_FILE, "w");
    for (int i = 0; i < count; i++) {
        if (i != choice - 1) {
            fprintf(file, "%s", lines[i]);
        }
    }
    fclose(file);
    printf("Password deleted successfully!\n");
}

int main() {
    srand(time(NULL));
    while (1) {
        printf("\n===== Password Manager =====\n");
        printf("1. Generate a new password\n");
        printf("2. View saved passwords\n");
        printf("3. Delete a saved password\n");
        printf("4. Exit\n");
        printf("Enter your choice: ");
        
        int choice;
        scanf("%d", &choice);
        getchar();
        
        if (choice == 1) {
            int num_passwords, length, include_upper, include_numbers, include_special;
            printf("How many passwords do you want to generate? ");
            scanf("%d", &num_passwords);
            printf("Enter password length: ");
            scanf("%d", &length);
            printf("0: No & 1: Yes\nInclude uppercase letters? (1/0): ");
            scanf("%d", &include_upper);
            printf("Include numbers? (1/0): ");
            scanf("%d", &include_numbers);
            printf("Include special characters? (1/0): ");
            scanf("%d", &include_special);
            getchar();
            
            char passwords[num_passwords][MAX_LENGTH];
            for (int i = 0; i < num_passwords; i++) {
                generate_password(passwords[i], length, include_upper, include_numbers, include_special);
                printf("%d. %s (Strength: %d/10)\n", i + 1, passwords[i], calculate_password_strength(passwords[i]));
            }
            
            int choice;
            printf("Enter the number of the password you want to save: ");
            scanf("%d", &choice);
            getchar();
            
            if (choice >= 1 && choice <= num_passwords) {
                char label[MAX_LENGTH];
                printf("Enter a label for this password: ");
                fgets(label, MAX_LENGTH, stdin);
                label[strcspn(label, "\n")] = '\0';
                save_password(label, passwords[choice - 1]);
            }
        } else if (choice == 2) {
            view_saved_passwords();
        } else if (choice == 3) {
            delete_saved_password();
        } else if (choice == 4) {
            printf("Exiting Password Manager. Goodbye!\n");
            break;
        } else {
            printf("Invalid choice!\n");
        }
    }
    return 0;
}