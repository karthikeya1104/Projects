import random as rd
import string


def get_input():
    l = int(input("Enter the Length Of Password You want : "))
    while l < 8:
        l = int(input("Your Password Length should be At least 8. Please Enter Again : "))
    c = int(input("Enter No of Passwords You want to Generate : "))
    while c < 1:
        c = int(input("You need to Generate At least One Password : "))
    return l, c


def generate_password(length):
    characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()"
    password = [
        rd.choice(string.ascii_lowercase),
        rd.choice(string.ascii_uppercase),
        rd.choice(string.digits),
        rd.choice(string.punctuation)
    ]
    for _ in range(length - 4):
        password.append(rd.choice(characters))
    rd.shuffle(password)
    return ''.join(password)


def generate_passwords(length, no_of_passwords):
    passwords = []
    for _ in range(no_of_passwords):
        passwords.append(generate_password(length))
    print('\n'.join(passwords))


def main():
    print("Welcome To Password Generator Application")
    length, no_of_passwords = get_input()
    generate_passwords(length, no_of_passwords)


if __name__ == '__main__':
    main()
