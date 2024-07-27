def encode(password):
    encodedPass = ""
    for i in password:
        x = int(i) + 3
        if x > 10:
            x -= 10
        encodedPass += str(x)
    return encodedPass

def decode(password):
    decodedPass = ""
    for i in password:
        x = int(i) - 3
        if x < 0:
            x = x + 10
        decodedPass += str(x)
    return decodedPass


def main():
    encoded = ""
    while(True):
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        print()
        option = int(input("Please enter an option:"))
        if option == 1:
            password = input("Please enter the password to encode: ")
            encoded = encode(password)
            print("Your password has been encoded and stored!")
        elif option == 2:
            print(f"The encoded password is {encoded}, and the original password is {decode(encoded)}")
        elif option == 3:
            quit()


if __name__ == "__main__":
    main()


