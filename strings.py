import string

def pig_latin_capitalize(word):
    if word[0].lower() in 'aeiou':
        output = f'{word}way'
    else:
        output = f'{word[1:]}{word[0]}ay'
    if word[0] in string.ascii_uppercase:
        output = output.capitalize()
    return output

pig_latin_capitalize('AIR')