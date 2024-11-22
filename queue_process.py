from collections import deque

input_words = input()

words = input_words.split()

queue = deque(words)

print(f"deque({list(queue)[::-1]})")

for word in queue:
    if  'a' in word:
        print(word)