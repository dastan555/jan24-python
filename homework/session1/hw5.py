import string 
while True:
    password = input("Enter a password: ")
    if len(password) < 8:
        print("password must be at least 8 characters ")
    elif not any(char.isupper() for char in password):
        print("password must contain at least one uppercase letter" )
    elif not any(char.islower() for char in password):
        print("password must contain at least one lowecase letter" )
    elif not any(char.isdigit() for char in password):
        print("password must contain at least one digit ")
    elif not any(char in string.punctuation for char in password):
        print("password must contain at least one special character ")
    else:
        print("password accepted")
        break


    