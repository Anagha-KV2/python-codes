def groupAnagrams(strs):
    anagrams = {}

    for word in strs:
        key = "".join(sorted(word))

        if key not in anagrams:
            anagrams[key] = []

        anagrams[key].append(word)

    return list(anagrams.values())

# User input
words = input("Enter words separated by spaces: ").split()

result = groupAnagrams(words)

print("Grouped Anagrams:")
for group in result:
    print(group)