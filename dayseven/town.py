def findJudge(n, trust):
    count = [0] * (n + 1)

    for a, b in trust:
        count[a] -= 1
        count[b] += 1

    for i in range(1, n + 1):
        if count[i] == n - 1:
            return i

    return -1


# Input
n = int(input("Enter number of people: "))
m = int(input("Enter number of trust relationships: "))

trust = []

for i in range(m):
    a, b = map(int, input("Enter trust pair (a b): ").split())
    trust.append([a, b])

print("Town Judge:", findJudge(n, trust))