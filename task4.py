import json

INPUT_FILE = "output.csv"

def csv_to_list_dict(filename, delimeter = ',', new_line = '\n') -> list[dict]:
    with open(filename, 'r') as f:
        headers = f.readline().split(",")
        headers = [n.rstrip() for n in headers]
        list_dict = []
        for line in f:
            line = line.split(',')
            line = [x.rstrip() for x in line]
            list_dict.append(dict(zip(headers, line)))
        return list_dict


print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))
