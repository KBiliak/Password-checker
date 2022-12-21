while True:
    with open("password.txt", "r") as file:
        content = file.readlines()

    password_input = input("Enter your password: ") + "\n"
    content.append(password_input)

    with open("password.txt", "w") as file:
        content1 = file.writelines(content)

    result = {}
    if len(password_input) >= 8:
        result["length"] = True
    else:
        result["length"] = False

    digit = False
    for i in password_input:
        if i.isdigit():
           digit = True

    result["digits"] = digit

    uppercase = False
    for i in password_input:
        if i.isupper():
            uppercase = True
    result["upper-case"] = uppercase

    print(result)
    print(result.values())

    if all(result.values()):
        print("Strong Password")
    else:
        print("Weak Password")
