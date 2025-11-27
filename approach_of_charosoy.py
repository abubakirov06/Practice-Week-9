def reformat_number(phone_number):
    number = phone_number.replace(' ', '').replace('-', '')
    new_list = []
    while len(number) > 4:
        new_list.append(number[:3])
        number = number[3:]
    
    if len(number) == 4:
        new_list.append(number[:2])
        new_list.append(number[2:])
    else:
        new_list.append(number)
    new_text = '-'.join(new_list)
    return new_text

print(reformat_number("123 456 789"))     # 9 digits -> 3-3-3
print(reformat_number("123-456-7890"))    # 10 digits -> 3-3-2-2 (4 remaining -> 2-2)
print(reformat_number("123 45 678"))      # 8 digits -> 3-3-2
print(reformat_number("12"))              # 2 digits -> 2
print(reformat_number("12345"))           # 5 digits -> 3-2
print(reformat_number("--1 23 4-5 6-7--"))