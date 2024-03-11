import secrets
import string

letters = string.ascii_letters
digits = string.digits
special_chars = string.punctuation
selection_list = letters + digits + special_chars

password_len = int(input("Enter the length of password:"))

while True:
    password = ''
    for i in range(password_len):
        password += ''.join(secrets.choice(selection_list))

    if (any(char.islower() for char in password) and
            any(char.isupper() for char in password) and
            any(char in digits for char in password) and
            any(char in special_chars for char in password)):
        break

print(password)
