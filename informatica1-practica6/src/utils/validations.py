def is_number(value) -> bool:
    for char in value:
        if char not in "0123456789":
            return False
    return True 

def is_alphabetic_string(text) -> bool:
    ascii_specials = \
        [32, 193, 201, 205, 211, 218, 225, 233, 237, 243, 250, 209, 241, 220, 252]
    if len(text) > 0:
        for char in text:
            ascii = ord(char)
            if not (65 <= ascii <= 90 or 97 <= ascii <= 122 or ascii in ascii_specials):
                return False
        return True
    else:
        return False
