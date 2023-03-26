def removeConsecutiveDuplicates(s):
    if len(s) < 2:
        return s
    if s[0] != s[1]:
        return s[0] + removeConsecutiveDuplicates(s[1:])
    return removeConsecutiveDuplicates(s[1:])


# This code is contributed by direwolf707
s1 = 'helloworldhello'
print(removeConsecutiveDuplicates(s1))  # geksforgeks
s2 = 'aabcca'
print(removeConsecutiveDuplicates(s2))  # ab