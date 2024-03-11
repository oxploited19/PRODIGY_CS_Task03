import random
import string
import sys

# Function to calculate password strength percentage
def password_strength_meter(password):
    criteria_list = [
        any(char.isupper() for char in password),
        any(char.islower() for char in password),
        any(char.isdigit() for char in password),
        any(not char.isalnum() for char in password)
    ]

    strength_score = sum(criteria_list)
    total_criteria = len(criteria_list)

    # Calculate percentage of strongness
    percentage_strongness = (strength_score / total_criteria) * 100
    return round(percentage_strongness)

# Function to provide feedback on password strength
def password_feedback(strength_percentage):
    if strength_percentage >= 80:
        return "\033[92mExcellent! Your password is very strong.\033[0m"
    elif 60 <= strength_percentage < 80:
        return "\033[93mGood! Your password is strong, but you can make it even stronger.\033[0m"
    elif 40 <= strength_percentage < 60:
        return "\033[96mFair. Your password is moderate. Consider adding more complexity.\033[0m"
    else:
        return "\033[91mWeak. Your password does not meet the recommended criteria. Please choose a stronger one.\033[0m"

# Function to generate strong password examples based on the user's input
def strong_password_examples(base_password):
    examples = []
    for _ in range(3):
        random_suffix = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=4))
        strong_password = base_password + random_suffix
        examples.append(strong_password)
    return examples

# Function to display a welcome message
def welcome_message():
    print("\n" + "=" * 40 + "\n")
    print("""
    \033[96m

┈╱▔▔▔▔▔▔╲┈╭━━━╮
▕┈╭━╮╭━╮┈▏┃Password-Complexity-Checker…┃
▕┈┃╭╯╰╮┃┈▏╰┳━━╯ by-Omar-Mahmood........|
▕┈╰╯╭╮╰╯┈▏┈┃ 
▕┈┈┈┃┃┈┈┈▏━╯ 
▕┈┈┈╰╯┈┈┈▏ 
▕╱╲╱╲╱╲╱╲▏


 \033[0m""")
    print("\033[92mEstimated Hacking Times:")
    print(" - Simple Password:   <1 second")
    print(" - Moderate Password:  Days to Weeks")
    print(" - Complex Password:  Years to Centuries\033[0m")

# Function to display a thank you message
def thank_you_message():
    print("\n" + "=" * 40 + "\n")
    print("""
    \033[95m

_ ___  o_.
 ___  /| !
___ ,/ |
__ ### |\  
__ ###/  \'
 ___|Thank-YOu|.\Prodigy-InfoTech\
   

    \033[0m""")

# Function to securely get password input with masking
def get_secure_password():
    try:
        while True:
            print("\n" + "=" * 40 + "\n")
            print("Password Criteria:")
            print("- Minimum length: 8 characters")
            print("- At least one uppercase letter")
            print("- At least one lowercase letter")
            print("- At least one digit")
            print("- At least one special character")
            print()

            while True:
                print("Enter a password: ", end='', flush=True)

                user_password = ""
                while True:
                    char = input()

                    if not char:
                        break  # Stop capturing characters if the user presses Enter
                    elif char == '\b':  # Backspace key pressed
                        if user_password:
                            user_password = user_password[:-1]
                            sys.stdout.write('\b \b')  # Erase the asterisk
                    else:
                        user_password += char
                        sys.stdout.write('*')
                    sys.stdout.flush()

                print()  # Move to the next line after the user presses Enter

                if user_password:
                    break
                else:
                    print("Password cannot be empty. Please enter a password.")

            strength_percentage = password_strength_meter(user_password)
            print("\033[F\033[K" + f"Password Strength: {strength_percentage:.2f}%")

            feedback = password_feedback(strength_percentage)
            print("\033[F\033[K" + feedback)

            examples = strong_password_examples(user_password)
            print("\nStrong password examples:")
            for example in examples:
                print(f"- {example}")

            check_another_password = input("\nDo you want to check another password for complexity? (yes/no): ").lower()
            if check_another_password != 'yes':
                break

    except ValueError as ve:
        print("\033[F\033[K" + "Error: " + str(ve))
    except KeyboardInterrupt:
        print("\nProcess interrupted. Exiting...")
    except Exception as e:
        print("\033[F\033[K" + "An unexpected error occurred: {}".format(e))

# Main program
try:
    welcome_message()
    get_secure_password()
    thank_you_message()
except Exception as e:
    print("\033[F\033[K" + "An unexpected error occurred: {}".format(e))
