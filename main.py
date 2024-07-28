def encode(password):
    encodedPass = ""
    for i in password:
        x = int(i[0]) + 3
        encodedPass += str(x)
    return encodedPass


def decode(password):
    decoded_pass = ""
    for i in password:
        x = int(i) - 3
        if x < 0:
            x = x + 10
        decoded_pass += str(x)
    return decoded_pass



