from pprint import pprint
d = [{"bin": bin(i), "dec": i, "hex": hex(i), "oct": oct(i)} for i in range(16)] # TODO решить с помощью list comprehension и распечатать его
pprint(d)