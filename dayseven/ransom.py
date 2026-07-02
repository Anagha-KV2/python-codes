def canConstruct(ransomNote, magazine):
    count = {}

    for ch in magazine:
        count[ch] = count.get(ch, 0) + 1

    for ch in ransomNote:
        if ch not in count or count[ch] == 0:
            return False
        count[ch] -= 1

    return True


ransomNote = input("Enter ransom note: ")
magazine = input("Enter magazine string: ")

if canConstruct(ransomNote, magazine):
    print("True")
else:
    print("False")