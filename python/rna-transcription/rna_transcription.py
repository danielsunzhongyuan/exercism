def to_rna(dna):
    m = {'G': 'C', 'C': 'G', 'T': 'A', 'A': 'U'}
    for x in set(dna):
        if x not in m.keys():
            return ""
    return "".join(map(lambda x: m[x], list(dna)))
