import random
import string


def get_random_password() -> str:
    s = (string.ascii_uppercase + string.ascii_lowercase + string.digits)
    password = random.sample(s, 8) # TODO написать функцию генерации случайных паролей
    return "".join(password)

print(get_random_password())
