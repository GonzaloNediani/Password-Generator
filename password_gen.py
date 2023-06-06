import random
import string

def generate_password(length):
    check_constraints(length)

    letters = generate_letters()
    numbers = generate_numbers()
    special = generate_special()

    password = letters + numbers + special
    print("generated password: ", password)
    return password

def generate_letters():
    return ''.join(random.choice(string.ascii_letters) for _ in range(3))

def generate_numbers():
    return ''.join(random.choice(string.digits) for _ in range(3))

def generate_special():
    return ''.join(random.choice(string.punctuation) for _ in range(3))

def check_constraints(length):
    if length < 9:
        raise ValueError("Minimum length for password is 9")
