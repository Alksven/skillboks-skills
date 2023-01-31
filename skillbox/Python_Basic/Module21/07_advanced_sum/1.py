def flatten(s):
    if s == []:
        return s
    if isinstance(s[0], list):
        return(flatten(s[0]) + flatten(s[1:]))
    return(s[:1] + flatten(s[1:]))
s = [67, [1, 2], [3, 4]]
print("Выпрямленный список: ", flatten(s))