# LinkedList implemented taken from: https://realpython.com/linked-lists-python/
# Practical Implementations of LinkedLists: queues/stacks/graphs.
from collections import deque # Deque (Deck) = Object from the collections module

# Quick implementation of a LinkedList in Python using deque
LinkedList = deque("abcdef")
print(LinkedList)
LinkedList.append("g")
print(LinkedList)
print(LinkedList.pop())
print(LinkedList)
LinkedList.appendleft("Q")
print(LinkedList)