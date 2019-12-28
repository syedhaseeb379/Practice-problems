def firstNotRepeatingCharacter(s):
    count = [0]*256
    for i in s:
        count[ord(i)] += 1
    for i in s:
        if count[ord(i)] == 1:
            return i
    return '_'
