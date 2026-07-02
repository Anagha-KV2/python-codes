class Solution:
    def isValid(self, s):
        stack = []
        pairs = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        for ch in s:
            if ch in "({[":
                stack.append(ch)
            else:
                if not stack or stack.pop() != pairs[ch]:
                    return False

        return len(stack) == 0


s = input("Enter parentheses string: ")

obj = Solution()

if obj.isValid(s):
    print("Valid Parentheses")
else:
    print("Invalid Parentheses")