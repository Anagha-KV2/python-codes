# Merge Intervals Program

n = int(input("Enter the number of intervals: "))

intervals = []

print("Enter the intervals (start end):")
for i in range(n):
    start, end = map(int, input().split())
    intervals.append([start, end])

# Sort intervals based on start time
intervals.sort()

merged = []

for interval in intervals:
    if not merged or merged[-1][1] < interval[0]:
        merged.append(interval)
    else:
        merged[-1][1] = max(merged[-1][1], interval[1])

print("Merged Intervals:")
for interval in merged:
    print(interval)