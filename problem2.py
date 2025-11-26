def reverse_words(sentence):
    new_list = sentence.split(' ')
    new_element = ''
    for i in range(len(new_list)):
        for c in new_list[i]:
            new_element = c + new_element
        new_list[i] = new_element
        new_element = ''
    new_string = ' '.join(new_list)
    return new_string

print(reverse_words("Hello, World"))
print(reverse_words("Python is fun!"))
print(reverse_words("This is a  test   with   multiple spaces"))
print(reverse_words("s'teL    ecitcarp"))