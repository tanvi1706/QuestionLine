import random
import string

ALPHANUMERIC_CHARS = string.ascii_lowercase + string.digits

def generate_random_string(chars=ALPHANUMERIC_CHARS, length=STRING_LENGTH):
    return "".join(random.choice(chars) for _ in range(length))