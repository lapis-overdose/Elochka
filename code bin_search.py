Вот код без комментариев:

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        if not self.head:
            self.head = Node(data)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(data)

    def display(self):
        current = self.head
        data_list = []
        while current:
            data_list.append(current.data)
            current = current.next
        return data_list

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        return None

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        return None

    def is_empty(self):
        return len(self.stack) == 0

    def display(self):
        return self.stack

class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, data):
        self.queue.append(data)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        return None

    def is_empty(self):
        return len(self.queue) == 0

    def display(self):
        return self.queue

class MinHeap:
    def __init__(self):
        self.heap = []

    def insert(self, val):
        self.heap.append(val)
        self._heapify_up(len(self.heap) - 1)

    def extract_min(self):
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)
        return root

    def _heapify_up(self, index):
        parent = (index - 1) // 2
        while index > 0 and self.heap[index] < self.heap[parent]:
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            index = parent
            parent = (index - 1) // 2

    def _heapify_down(self, index):
        smallest = index
        left = 2 * index + 1
        right = 2 * index + 2
        if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
            smallest = left
        if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
            smallest = right
        if smallest != index:
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            self._heapify_down(smallest)

    def display(self):
        return self.heap

def to_lower_case(s):
    return s.lower()

def recurs(left, right, guessing_num, steps, lies_list, steps_array, guess_stack, response_queue):
    if left > right:
        print("Your number is outside the range!")
        return -1
    steps += 1
    steps_array.append(steps)
    mid = left + (right - left) // 2
    guess_stack.push(mid)
    response = input(f"Is your number {mid}? (enter 'yes', 'higher', or 'lower'): ")
    response = to_lower_case(response)
    response_queue.enqueue(response)
    if response == "yes":
        if mid == guessing_num:
            return mid
        else:
            print("You're lying! I caught you!")
            lies_list.append("Lie Detected")
            return -1
    elif response == "higher":
        if mid >= guessing_num:
            print(f"You're lying! Your number can't be higher than {mid}!")
            lies_list.append("Lie Detected")
            return -1
        return recurs(mid + 1, right, guessing_num, steps, lies_list, steps_array, guess_stack, response_queue)
    elif response == "lower":
        if mid <= guessing_num:
            print(f"You're lying! Your number can't be lower than {mid}!")
            lies_list.append("Lie Detected")
            return -1
        return recurs(left, mid - 1, guessing_num, steps, lies_list, steps_array, guess_stack, response_queue)
    else:
        print("Invalid input. Please answer 'yes', 'higher', or 'lower'.")
        return recurs(left, right, guessing_num, steps, lies_list, steps_array, guess_stack, response_queue)

left = 0
right = 100
steps_array = []
lies_list = LinkedList()
guess_stack = Stack()
response_queue = Queue()
priority_heap = MinHeap()

try:
    guessing_num = int(input("Please enter your number (between 0 and 100): "))
    if guessing_num < 0 or guessing_num > 100:
        print("Invalid number. Please choose a number between 0 and 100.")
    else:
        result = recurs(left, right, guessing_num, 0, lies_list, steps_array, guess_stack, response_queue)
        if result != -1:
            print(f"I guessed your number! It's {result}!")
            print(f"It took only {len(steps_array)} steps to guess your number.")
        else:
            print("Game over, YOU LOST!")
        print(f"Steps taken during the game: {steps_array}")
        print(f"Count of lies detected: {len(lies_list.display())}")
        if lies_list.display():
            print(f"Lies detected at these points: {lies_list.display()}")
        print(f"All guesses (stack): {guess_stack.display()}")
        print(f"Responses (queue): {response_queue.display()}")
        for i in range(5):
            priority_heap.insert(i * 10)
        print(f"Heap after insertions: {priority_heap.display()}")
        print(f"Extracted min from heap: {priority_heap.extract_min()}")
except ValueError:
    print("Invalid input. Please enter a valid number.")
```