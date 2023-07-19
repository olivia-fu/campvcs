key = int(input("key: "))
plaintext = input("plaintext: ")

for char in plaintext:
    if char.isupper():
        print(chr((ord(char) - 65 + key) % 26 + 65), end="")
    elif char.islower():
        print(chr((ord(char) - 97 + key) % 26 + 97), end="")
    else:
        print(char, end="")
print("")