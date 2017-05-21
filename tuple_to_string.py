def tuple_to_string(tuple):
    string = ''
    for i in range(0, len(tuple)):
        num = tuple[i]
        char = chr(num)
        string += str(char)
    return string