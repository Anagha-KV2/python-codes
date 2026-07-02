from collections import Counter

def is_anagram(s1, s2):
    return Counter(s1.lower()) == Counter(s2.lower())

print(is_anagram("listen", "silent"))   # True
print(is_anagram("running", "code"))    # False