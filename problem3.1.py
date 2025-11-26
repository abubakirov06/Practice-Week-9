def reformat_number(phone_number):
    new_string = phone_number.replace(' ', '').replace('-', '')
    new_list = []
    checker = 0
    element = ''
    123-456-7890
    123455
    if len(new_string) % 3 == 1:
        if len(new_string) == 1: return int(new_string)
        elif len(new_string) == 4:
            for c in new_string:
                element += c
                if len(element) == 2:
                    new_list.append(element)
                    element = ''
        else: # 123,45,67   123, 456, 78, 90
            for c in new_string[:-4]:
                element += c
                if len(element) == 3:
                    new_list.append(element)
                    element = ''
            for ch in new_string[-4:]:
                element += ch
                if len(element) == 2:
                    new_list.append(element)
                    element = ''    

       # 123, 45        123, 456, 78
    elif len(new_string) % 3 == 2:
        if len(new_string) == 2: new_list.append(new_string)
        else:
            for c in new_string[:-2]:
                element += c
                if len(element) == 3:
                    new_list.append(element)
                    element = ''
            for ch in new_string[-2:]:
                element += ch
                if len(element) == 2:
                    new_list.append(element)
                    element = ''
           
    else:
        for c in new_string:
            element += c
            if len(element) == 3:
                new_list.append(element)
                element = ''

    returning = '-'.join(new_list)
    return returning

print(reformat_number("123 456 789"))     # 9 digits -> 3-3-3
print(reformat_number("123-456-7890"))    # 10 digits -> 3-3-2-2 (4 remaining -> 2-2)
print(reformat_number("123 45 678"))      # 8 digits -> 3-3-2
print(reformat_number("12"))              # 2 digits -> 2
print(reformat_number("12345"))           # 5 digits -> 3-2
print(reformat_number("--1 23 4-5 6-7--"))