def is_isogram(word):
    word_dict = dict()
    for c in word:
        c = c.lower()
        if ord('a') <= ord(c) <= ord('z'):
            word_dict[c] = word_dict.get(c, 0) + 1
            if word_dict[c] >= 2:
                return False
    return True
