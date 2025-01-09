import heapq

class Node:
    """Node class for the linked list."""
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    """Simple linked list to track lies."""
    def __init__(self):
        self.head = None

    def append(self, data):
        """Add a new node with the given data."""
        if not self.head:
            self.head = Node(data)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(data)

    def display(self):
        """Display all nodes' data."""
        current = self.head
        data_list = []
        while current:
            data_list.append(current.data)
            current = current.next
        return data_list

class Stack:
    """Stack implementation using a list (LIFO)."""
    def __init__(self):
        self.stack = []

    def push(self, data):
        """Push data onto the stack."""
        self.stack.append(data)

    def pop(self):
        """Pop data from the stack."""
        if not self.is_empty():
            return self.stack.pop()
        return None

    def peek(self):
        """Peek at the top item of the stack."""
        if not self.is_empty():
            return self.stack[-1]
        return None

    def is_empty(self):
        """Check if the stack is empty."""
        return len(self.stack) == 0

    def display(self):
        """Display the stack contents."""
        return self.stack

class Queue:
    """Queue implementation using a list (FIFO)."""
    def __init__(self):
        self.queue = []

    def enqueue(self, data):
        """Add data to the queue."""
        self.queue.append(data)

    def dequeue(self):
        """Remove and return the front item of the queue."""
        if not self.is_empty():
            return self.queue.pop(0)
        return None

    def is_empty(self):
        """Check if the queue is empty."""
        return len(self.queue) == 0

    def display(self):
        """Display the queue contents."""
        return self.queue

# Function to convert input to lowercase
def to_lower_case(s):
    return s.lower()

def recurs(left, right, guessing_num, steps, lies_list, steps_array, guess_stack, response_queue):
    # Base case: If the range is invalid
    if left > right:
        print("Your number is outside the range!")
        return -1

    # Increment step counter
    steps += 1
    steps_array.append(steps)

    # Calculate the midpoint
    mid = left + (right - left) // 2

    # Track guesses in the stack
    guess_stack.push(mid)

    # Ask user for feedback
    response = input(f"Is your number {mid}? (enter 'yes', 'higher', or 'lower'): ")
    response = to_lower_case(response)
    response_queue.enqueue(response)

    # If the user confirms the number
    if response == "yes":
        if mid == guessing_num:
            return mid
        else:
            print("You're lying! I caught you!")
            lies_list.append("Lie Detected")
            return -1
    # If the user indicates the number is higher
    elif response == "higher":
        if mid >= guessing_num:
            print(f"You're lying! Your number can't be higher than {mid}!")
            lies_list.append("Lie Detected")
            return -1
        return recurs(mid + 1, right, guessing_num, steps, lies_list, steps_array, guess_stack, response_queue)
    # If the user indicates the number is lower
    elif response == "lower":
        if mid <= guessing_num:
            print(f"You're lying! Your number can't be lower than {mid}!")
            lies_list.append("Lie Detected")
            return -1
        return recurs(left, mid - 1, guessing_num, steps, lies_list, steps_array, guess_stack, response_queue)
    # Handle invalid input
    else:
        print("Invalid input. Please answer 'yes', 'higher', or 'lower'.")
        return recurs(left, right, guessing_num, steps, lies_list, steps_array, guess_stack, response_queue)

# Heap Operations
class MinHeap:
    """Min-Heap implementation."""
    def __init__(self):
        self.heap = []

    def insert(self, val):
        """Insert value into the heap."""
        heapq.heappush(self.heap, val)

    def extract_min(self):
        """Extract the minimum value from the heap."""
        if self.heap:
            return heapq.heappop(self.heap)
        return None

    def display(self):
        """Display the heap as a list."""
        return self.heap

# Game setup
left = 0
right = 100

# Tracking structures
steps_array = []  # Array to track steps
lies_list = LinkedList()  # Linked List to track lies
guess_stack = Stack()  # Stack to track guesses
response_queue = Queue()  # Queue to track responses
priority_heap = MinHeap()  # Min-Heap to track priority guesses

try:
    # Get the number to guess
    guessing_num = int(input("Please enter your number (between 0 and 100): "))
    if guessing_num < 0 or guessing_num > 100:
        print("Invalid number. Please choose a number between 0 and 100.")
    else:
        # Start the guessing game
        result = recurs(left, right, guessing_num, 0, lies_list, steps_array, guess_stack, response_queue)
        if result != -1:
            print(f"I guessed your number! It's {result}!")
            print(f"It took only {len(steps_array)} steps to guess your number.")
        else:
            print("Game over, YOU LOST!")

        # Display tracked scores and history
        print(f"Steps taken during the game: {steps_array}")
        print(f"Guesses made (stack): {guess_stack.display()}")
        print(f"Responses recorded (queue): {response_queue.display()}")
        print(f"Count of lies detected: {len(lies_list.display())}")
        if lies_list.display():
            print(f"Lies detected at these points: {lies_list.display()}")

        # Heap demo
        for i in range(5):
            priority_heap.insert(i * 10)
        print(f"Heap after insertions: {priority_heap.display()}")
        print(f"Extracted min from heap: {priority_heap.extract_min()}")
except ValueError:
    print("Invalid input. Please enter a valid number.")
