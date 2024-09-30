import re

def is_valid_password(password):
    # Check password length
    if len(password) < 6 or len(password) > 10:
        return False
    
    # Check for at least 1 lowercase letter
    if not re.search("[a-z]", password):
        return False
    
    # Check for at least 1 uppercase letter
    if not re.search("[A-Z]", password):
        return False
    
    # Check for at least 1 digit
    if not re.search("[0-9]", password):
        return False
    
    # Check for at least 1 special character from [$#@]
    if not re.search("[$#@]", password):
        return False
    
    return True

def main():
    password = input("Create a new password: ")
    
    if is_valid_password(password):
        print("Password is valid!")
    else:
        print("Password is invalid. Please ensure it meets the requirements.")

if __name__ == "__main__":
    main()
