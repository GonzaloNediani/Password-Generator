import random
import string

def generate_password(length):
    check_constraints(length)

    letters = generate_letters()
    while has_unique_characters(letters) == False:
        letters = generate_letters()
    
    numbers = generate_numbers()
    while has_unique_characters(numbers) == False:
        numbers = generate_numbers()

    special = generate_special()
    while has_unique_characters(special) == False:
        special = generate_special()

    password = letters + numbers + special
    password = shuffle_characters(password)

    print("Generated password is: ", password)

    return password

def generate_letters():
    letters = ''.join(random.choice(string.ascii_letters) for _ in range(3))
    letters = letters[0].upper() + letters[1].lower() + letters[2]
    return letters

def generate_numbers():
    numbers = ''.join(random.choice(string.digits) for _ in range(3))
    return numbers

def generate_special():
    return ''.join(random.choice(string.punctuation) for _ in range(3))

def has_unique_characters(password):
    return len(set(password)) == len(password)

def shuffle_characters(password):
    char_list = list(password)
    random.shuffle(char_list)
    shuffled_string = ''.join(char_list)
    return shuffled_string

def check_constraints(length):
    if length < 9:
        raise ValueError("Minimum length for password is 9")
