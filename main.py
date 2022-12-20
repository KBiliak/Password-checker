while True:
    with open("password.txt", "r") as file:
        content = file.readlines()

    password_input = input("Enter your password: ") + "\n"
    content.append(password_input)

    with open("password.txt", "w") as file:
        content1 = file.writelines(content)

    length = len(password_input)
    result = []
    if length >= 8:
        result.append(True)
    else:
        result.append(False)

    digit = False
    for i in password_input:
        if i.isdigit():
            digit = True

    result.append(digit)

    uppercase = False
    for i in password_input:
        if i.isupper():
            uppercase = True
    result.append(uppercase)

    if all(result):
        print("Strong Password")
    else:
        print("Weak Password")
