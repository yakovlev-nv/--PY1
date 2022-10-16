def get_count_char(str_):
    d = {i: str_.lower().count(i) for i in str_.lower() if i.isalpha()}
    return d  # TODO посчитать количество каждой буквы в строке в аргументе str_

main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
d = get_count_char(main_str)

def percentage_char(d):
    d1 = {char: round(d[char]/len(main_str)*100, 2) for char in d}
    return (d1)

print(get_count_char(main_str))
