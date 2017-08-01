import string
def rotate(orig, offset):
    ret = ""
    for c in orig:
        if c in string.ascii_lowercase:
            ret += chr(ord('a') + (ord(c) - ord('a') + offset) % 26)
        elif c in string.ascii_uppercase:
            ret += chr(ord('A') + (ord(c) - ord('A') + offset) % 26)
        else:
            ret += c
    return ret
