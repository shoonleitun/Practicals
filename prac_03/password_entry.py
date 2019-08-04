"""Shoon Lei Tun"""
MINIMUM_LENGTH = 5
def main():
    password = input("Enter password of at least {} characters: ".format(MINIMUM_LENGTH))
    while len(password) < MINIMUM_LENGTH:
        password = input("Enter password of at least {} characters: ".format(MINIMUM_LENGTH))
    get_password(password)


def get_password(passwd):
    print('*' * len(passwd))

main()