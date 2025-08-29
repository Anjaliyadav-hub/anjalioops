def replace_character(original_string, target_char, replacement_char):
    new_string = ""
    for char in original_string:
        if char == target_char:
            new_string += replacement_char
        else:
            new_string += char
    return new_string
text = "banana"
result = replace_character(text, 'a', 'o')
print("Original:", text)
print("Modified:", result)