def dailyTemperatures(temperatures):
    n = len(temperatures)
    answer = [0] * n
    stack = []

    for i in range(n):
        while stack and temperatures[i] > temperatures[stack[-1]]:
            index = stack.pop()
            answer[index] = i - index

        stack.append(i)

    return answer


# Input
temperatures = list(map(int, input("Enter temperatures separated by spaces: ").split()))

result = dailyTemperatures(temperatures)

print("Output:", result)