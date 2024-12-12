import random
print("\nChoose the components of your password: ")
print("Upper case letters - 1")
print("Lower case letters - 2")
print("Numbers            - 3")
print("Special symbols    - 4")
print("\nIf you want to choose multiple options, write the numbers together, e.g., 1234")

def operation():
    global symbols_password
    symbols_password = ''  # reset symbols_password before adding new symbols
    if "1" in sym_in_pass:
        symbols_password += upper_case_letters
    if "2" in sym_in_pass:
        symbols_password += lower_case_letters
    if "3" in sym_in_pass:
        symbols_password += numbers
    if "4" in sym_in_pass:
        symbols_password += special_symbols

Continue = True
password = ''
symbols_password = ''
upper_case_letters = 'QWERTYUIOPASDFGHJKLZXCVBNM'
lower_case_letters = 'qwertyuiopasdfghjklzxcvbnm'
numbers = '1234567890'
special_symbols = '!@#$%^&*(){}[]'
while Continue:
    sym_in_pass = input("Enter the components:     ")
    length = int(input("Enter the password length:     "))
    operation()
    for i in range(length):
        symbol = random.choice(symbols_password)
        password += symbol
    print("Generated password: ", password)
    Continue = input("Continue? yes|no:     ")
    if Continue.lower() == "yes":
        password = '' # reset password
        continue
    elif Continue.lower() == "no":
        Continue = False # exit
