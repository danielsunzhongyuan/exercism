def detect_anagrams(word, candidates):
    return [x for x in candidates if ''.join(sorted(x.lower())) == ''.join(sorted(word.lower())) and x.lower() != word.lower()]
