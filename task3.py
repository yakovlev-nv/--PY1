import random
def get_unique_list_numbers() -> list[int]:
    l = []

    while len(l)!=15:
        random_int = random.randint(-10, 10)
        if random_int not in l:
            l.append(random_int)
    return l




list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
