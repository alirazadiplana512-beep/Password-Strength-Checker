import string

password = input("Enter Password: ")

score = 0

# Length Check
if len(password) >= 8:
    score += 1

# Uppercase Check
if any(char.isupper() for char in password):
    score += 1

# Lowercase Check
if any(char.islower() for char in password):
    score += 1

# Number Check
if any(char.isdigit() for char in password):
    score += 1

# Special Character Check
if any(char in string.punctuation for char in password):
    score += 1

# Strength Evaluation
if score <= 2:
    strength = "Weak Password"
elif score <= 4:
    strength = "Medium Password"
else:
    strength = "Strong Password"

print("\nPassword Strength:", strength)

# Security Suggestions
if strength != "Strong Password":
    print("\nRecommendations:")

    if len(password) < 8:
        print("- Use at least 8 characters.")

    if not any(char.isupper() for char in password):
        print("- Add uppercase letters.")

    if not any(char.isdigit() for char in password):
        print("- Add numbers.")

    if not any(char in string.punctuation for char in password):
        print("- Add special characters.")