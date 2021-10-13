s = input()


def conversion(s):
    split_string = s.split(":")
    if "AM" in s:
        if "12" in s:
            return f'00:{":".join(split_string[1:]).replace("AM", "")}'
        else:
            return s.replace("AM", "")
    elif "PM" in s:
        if "12" not in s:
            return f'{int(split_string[0]) + 12}:{":".join(split_string[1:]).replace("PM", "")}'
        if "12" in s:
            return f'12:{":".join(split_string[1:]).replace("PM", "")}'


print(conversion(s))
