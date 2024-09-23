
import getpass

def password_protect():
    correct_password = "12345"
    password = getpass.getpass("Enter password: ")
    if password == correct_password:
        print("Access Granted")
    else:
        print("Access Denied")

# Example
password_protect()
