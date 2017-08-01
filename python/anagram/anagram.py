def detect_anagrams(word, candidates):
    return [x for x in candidates if ''.join(sorted(x)) == ''.join(sorted(word))]
