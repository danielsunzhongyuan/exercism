def distance(dna1, dna2):
    if len(dna1) != len(dna2):
        raise(ValueError)
    ret = 0
    for i in range(len(dna1)):
        if dna1[i] != dna2[i]:
            ret += 1
    return ret 
