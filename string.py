text="i am from Palakkad"
print(text)
print(text[-1])
print(text[:4])
print(text[::-2])

print(text.split(" "))
print(text.strip(" "))
new_text = "so far it's been a great climate"
new_list = new_text.split(" ")
str = " ".join(new_list)
print(str)

print(str.find("climate"))
print(str.count("a"))

text1="Palakkad"
text1_upper=text1.upper()
print(text1_upper)
print(text1.strip())
text2=text.split(" ")
print(text2)


text="Anagha"
if text.isalpha():
    print(f"'{text}' is a letter")
elif text.isdigit():
    print(f"'{text}' is a number")
else:
        print(f"'{text}' is a symbol")

