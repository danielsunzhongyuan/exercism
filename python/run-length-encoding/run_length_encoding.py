import string

def decode(rle):
    i, length = 0, len(rle)
    ret = ""
    while i < length:
        if rle[i] in string.digits:
            tmp = 1
            while rle[i+tmp] in string.digits:
                tmp += 1
            ret += rle[i+tmp] * int(rle[i:i+tmp])
            i += tmp + 1
        else:
            ret += rle[i]
            i += 1
    return ret 


def encode(orig_string):
    ret = ""
    i, length = 0, len(orig_string)
    while i < length:
        j = i + 1
        tmp = 1
        while j < length:
           if orig_string[j] == orig_string[i]:
               tmp += 1
               j += 1
           else:
               break
        if tmp == 1:
            ret += orig_string[i]
        else:
            ret += str(tmp) + orig_string[i]
        i += tmp
    return ret
