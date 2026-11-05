from collections import deque

stack = []
queue = deque()

s = input("Enter a word or number: ").lower()

for ch in s:
    if ch.isalnum():
        stack.append(ch)
        queue.append(ch)

is_palindrome = True

while stack:
    if stack.pop() != queue.popleft():
        is_palindrome = False
        break

if is_palindrome:
    print("Palindrome")
else:
    print("Not a Palindrome")