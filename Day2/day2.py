def read_file(file_name: str):
    with open(file_name, "r") as file:
        return file.read().split('\n')

content_list = read_file("list.txt")



def submarine_position(list):
    aim = 0
    position = 0
    depth = 0

    for string in list:
        if 'down' in string:
           aim += int(string[-1])

        elif 'up' in string:
            aim -= int(string[-1])

        elif 'forward' in string:
            position += int(string[8])
            depth += int(string[8]) * aim

        else:
            pass

    return position*depth

result = submarine_position(content_list)

print(result)