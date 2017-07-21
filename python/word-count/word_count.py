import string

def word_count(sentence):
    ret = dict()
    i, length = 0, len(sentence)
    while i < length:
        tmp = ""
        while sentence[i].lower() in string.lowercase + string.digits:
            tmp += sentence[i].lower()
            i += 1
            if i >= length:
                break
        if tmp:
            ret[tmp] = ret.get(tmp, 0) + 1
        i += 1
    return ret
