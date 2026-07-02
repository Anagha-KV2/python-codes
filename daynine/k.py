from collections import Counter

def topKFrequent(nums, k):
    count = Counter(nums)
    return [num for num, freq in count.most_common(k)]

# Test
nums = [1, 1, 1, 2, 2, 3]
k = 2

print("Input:", nums)
print("k =", k)
print("Output:", topKFrequent(nums, k))