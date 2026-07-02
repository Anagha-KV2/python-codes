def contains_duplicate(nums):
    seen = set()

    for num in nums:
        if num in seen:
            return True
        seen.add(num)

    return False


nums = list(map(int, input("Enter numbers separated by space: ").split()))

if contains_duplicate(nums):
    print("True")
else:
    print("False")