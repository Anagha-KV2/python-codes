# Majority Element Program

n = int(input("Enter the number of elements: "))

arr = list(map(int, input("Enter the elements: ").split()))

# Boyer-Moore Voting Algorithm
candidate = None
count = 0

for num in arr:
    if count == 0:
        candidate = num
    count += 1 if num == candidate else -1

# Verify the candidate
if arr.count(candidate) > n // 2:
    print("Majority Element is:", candidate)
else:
    print("No Majority Element")