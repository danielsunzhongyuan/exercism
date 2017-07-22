import string

def hey(hi):
    hi = hi.strip()
    if hi == "":
        return "Fine. Be that way!"
    elif len(filter(lambda x: x in string.uppercase, list(hi))) > 0 and len(filter(lambda x: x in string.lowercase, list(hi))) == 0:
        return "Whoa, chill out!"
    elif hi.endswith("?"):
        return "Sure."
    else:
        return "Whatever."
