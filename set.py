s2 = {1,2,3,4}
print(s2)
s3 = {10,"hello",3.14,True}
print(s3)
s4 = {1,2,3,4,5}
print(s4)
s2.add(20)
print(s2)


nums = (10,11,12)
print(len(nums))
print(max(nums))
print(min(nums))
print(sum(nums))


nums_list = list(nums)
print()

tuple = (1,2,3,4)
print(tuple[3])
print(tuple.index(2))

print(tuple.count(1))


numbers = (10,20,30,40)
print([numbers[0]])
print([numbers[-2]])
print([numbers[1:4]])


t = (5,6,7,8,9)
print(max(t))
print(min(t))
print(sum(t))


person = "Alice", 25, "Engineer"
name, age, profession = person
print(name)
print(age)
print(profession)


d2={"name":"Alice", "age":25, "city": "Delhi"}
d3={"name":"Anagha", "age":22, "city":"Palakkad"}
print(d3)
d3 = dict(id=101,branch="cse")
print(d3)

#nested dict
d4 = {"student":{"name":"Bob","age":23},
"marks":{"maths":98, "science":85}}
print(d4)



