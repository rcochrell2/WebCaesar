def encrypt(text, rotation):
    result = ''
    for ch in text:
        if ch == '':
            result = result + ''
        else:
            new_char = rotate_character(ch,rotation)
            result = result + str(new_char)
    return result

def alphabet_position(letter):
    if letter in string.ascii_lowercase:
        return string.ascii_lowercase.find(letter)
    elif letter in string.ascii_uppercase:
        return string.ascii_uppercase.find(letter)
    else:
        return none


def rotate_character(char, rotation):
    if char.isalpha():
        alphabet = ord(char) + rotation
        if alphabet > ord('z'):
            alphabet = alphabet - 26
        elif char.isupper():
            if alphabet > ord('Z'):
                alphabet = alphabet - 26
        return chr(alphabet)
    else:
        return char
