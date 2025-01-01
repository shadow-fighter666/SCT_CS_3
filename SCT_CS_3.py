import re

def check_password_strength(password):
    # Criteria for password strength
    length_criteria = len(password) >= 8
    uppercase_criteria = bool(re.search(r'[A-Z]', password))
    lowercase_criteria = bool(re.search(r'[a-z]', password))
    number_criteria = bool(re.search(r'\d', password))
    special_char_criteria = bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password))
    
    # Feedback and suggestions
    feedback = []
    if not length_criteria:
        feedback.append("- Password should be at least 8 characters long.")
    if not uppercase_criteria:
        feedback.append("- Password should contain at least one uppercase letter.")
    if not lowercase_criteria:
        feedback.append("- Password should contain at least one lowercase letter.")
    if not number_criteria:
        feedback.append("- Password should contain at least one number.")
    if not special_char_criteria:
        feedback.append("- Password should contain at least one special character.")
    
    # Assessing strength
    strength_score = sum([length_criteria, uppercase_criteria, lowercase_criteria, number_criteria, special_char_criteria])
    if strength_score == 5:
        strength = "Strong"
    elif strength_score >= 3:
        strength = "Moderate"
    else:
        strength = "Weak"
    
    return strength, feedback

# Ask for user input
user_password = input("Enter your password: ")
strength, feedback = check_password_strength(user_password)

# Display the result
print(f"\nPassword Strength: {strength}")
if feedback:
    print("Suggestions to improve your password:")
    for suggestion in feedback:
        print(suggestion)