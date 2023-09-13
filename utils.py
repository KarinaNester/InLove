from hashlib import sha512
import random
import string


def generate_random_string(lenght: int)->str:
    salt_list = random.choices(string.ascii_letters, k=lenght)
    salt = ""
    for n in salt_list:
        salt = salt + n
    return salt


def encode_password(password: str, salt: str)-> str:
    return sha512(f"{salt}{password}".encode()).hexdigest()