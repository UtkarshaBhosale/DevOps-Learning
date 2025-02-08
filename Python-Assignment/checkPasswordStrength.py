import re

def check_password_strength(password):
    
    # Checks the strength of a password.
    
    check_criteria = []
    
    if len(password) < 8:
        check_criteria.append("Password must contains at least 8 characters.")
    if not re.search("[A-Z]", password):
        check_criteria.append("Password should have at least one uppercase letter.")
    if not re.search("[a-z]", password):
        check_criteria.append("Password should have at least one lowercase letter.")
    if not re.search("[0-9]", password):
        check_criteria.append("Password should have at least one number")
    if not re.search("[@#$%^&*]", password):
        check_criteria.append("'Password should have at least one special character.")
    
    if check_criteria:
        return False, "Weak Password:\n" + "\n".join(check_criteria)
    return True, "Strong Password!"

if __name__ == "__main__":
    user_password = input("Enter a password to check its strength: ")
    status, message = check_password_strength(user_password)  
    print(message)  

