import random
import string

BASE_CHAR_AMOUNT = 3

def generate_password(complexity):
    check_constraints(complexity)

    letters = generate_letters(complexity)
    numbers = generate_numbers(complexity)
    special = generate_special(complexity)

    password = letters + numbers + special
    password = shuffle_characters(password)

    print("Generated password is: ", password)

    return password

def generate_letters(complexity):
    letters = 'AAA'
    while has_unique_characters(letters) == False:
        letters = ''.join(random.choice(string.ascii_letters) for _ in range(BASE_CHAR_AMOUNT * complexity))
    letters = letters[0].upper() + letters[1].lower() + letters[2:]
    return letters

def generate_numbers(complexity):
    numbers = '000'
    while has_unique_characters(numbers) == False:
        numbers = ''.join(random.choice(string.digits) for _ in range(BASE_CHAR_AMOUNT * complexity))
    return numbers

def generate_special(complexity):
    special = '***'
    while has_unique_characters(special) == False:
        special = ''.join(random.choice(string.punctuation) for _ in range(BASE_CHAR_AMOUNT * complexity))
    return special

def has_unique_characters(password):
    return len(set(password)) == len(password)

def shuffle_characters(password):
    char_list = list(password)
    random.shuffle(char_list)
    shuffled_string = ''.join(char_list)
    return shuffled_string

def check_constraints(complexity):
    if complexity < 1 or complexity > 3:
        raise ValueError("Please enter a complexity between 1 and 3")
