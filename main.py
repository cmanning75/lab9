def encode(password):
    encodedPass = ""
    for i in password:
        x = int(i[0]) + 3
        encodedPass += str(x)
    return encodedPass




