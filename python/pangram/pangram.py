def is_pangram(sentence):
    letters = [False] * 26
    for c in sentence:
        c = c.lower()
        if ord('a') <= ord(c) <= ord('z'):
            tmp = ord(c) - ord('a')
            letters[tmp] = True
    return all(letters)
