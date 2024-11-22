from collections import deque

input_numbers = input()

numbers = list(map(int, input_numbers.split()))

stack = deque(numbers)

print(f"deque({list(stack)})")

while stack:
    print(stack.pop() * 2)