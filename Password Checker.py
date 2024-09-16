
import re

def check_password_strength(password):
    
    length_check = len(password) >= 8
    lowercase_check = re.search(r'[a-z]', password) is not None
    uppercase_check = re.search(r'[A-Z]', password) is not None
    digit_check = re.search(r'[0-9]', password) is not None
    special_char_check = re.search(r'[\W_]', password) is not None

    strength = 0
    if length_check:
        strength += 1
    if lowercase_check:
        strength += 1
    if uppercase_check:
        strength += 1
    if digit_check:
        strength += 1
    if special_char_check:
        strength += 1

    
    if strength == 5:
        return "Very Strong"
    elif strength == 4:
        return "Strong"
    elif strength == 3:
        return "Moderate"
    else:
        return "Weak"

password = input("Enter your password: ")

strength = check_password_strength(password)
print(f"Your password strength is: {strength}")
