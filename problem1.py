def are_anagrams(string1, string2):
    new_list1 = []
    new_list2 = []
    string3, string4 = string1.strip().lower(), string2.strip().lower()
    for c in string3:
        if not c in ' , . : ?':
            new_list1.append(c)
    for ch in string4:
        if not ch in ' , . : ?':
            new_list2.append(ch)
    new_list1.sort()
    new_list2.sort()
    #print(new_list1, '\n', new_list2)
    return new_list1 == new_list2

print(are_anagrams("Listen", "Silent"))
print(are_anagrams("The Morse Code", "Here come dots"))
print(are_anagrams("Astronomer", "Moon starer"))
print(are_anagrams("Hello", "World"))
print(are_anagrams("Dormitory", "Dirty room."))
    

    
