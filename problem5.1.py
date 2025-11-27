def parse_markdown(text):
    new_text = ''
    counter = 0
    if '**_' in text:
            return False
    '**this**'
    for i in range(len(text)):
        if text[i] == '*':
            if counter == 0:
                new_text += '<b>'
                counter +=1
            elif counter == 1:
                new_text += ''
                counter += 1
            elif counter == 3:
                new_text += ''
                counter = 0
            elif counter == 2:
                new_text += '</b>'
                counter += 1 

        elif text[i] == '_':
            if counter == 0:
                new_text += '<i>'
                counter +=1
            else:
                new_text += '</i>'
                counter = 0
        else:
            new_text += text[i]
    return new_text

print()
print(parse_markdown("This is **bold** text."))
print(parse_markdown("Hello _world_."))
print(parse_markdown("Make **this** bold and _this_ italic."))
print(parse_markdown("No formatting here."))
print(parse_markdown("**Bold** at start."), '\n')
