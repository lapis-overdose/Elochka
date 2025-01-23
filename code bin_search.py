import heapq

# Classes (Node, LinkedList, Stack, Queue, MinHeap) remain the same
# The recursive guessing game remains the same

def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)

def merge(left, right):
    merged = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged

def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)

def linear_search(arr, target):
    for index, value in enumerate(arr):
        if value == target:
            return index
    return -1

if __name__ == "__main__":
    data = [64, 34, 25, 12, 22, 11, 90]
    print("Original Data:", data)

    bubble_sorted = bubble_sort(data.copy())
    print("Bubble Sort Result:", bubble_sorted)

    merge_sorted = merge_sort(data.copy())
    print("Merge Sort Result:", merge_sorted)

    quick_sorted = quick_sort(data.copy())
    print("Quick Sort Result:", quick_sorted)

    search_target = 22
    search_result = linear_search(data, search_target)
    if search_result != -1:
        print(f"Linear Search: Found {search_target} at index {search_result}")
    else:
        print(f"Linear Search: {search_target} not found")

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
            print(f"Guesses made (stack): {guess_stack.display()}")
            print(f"Responses recorded (queue): {response_queue.display()}")
            print(f"Count of lies detected: {len(lies_list.display())}")
            if lies_list.display():
                print(f"Lies detected at these points: {lies_list.display()}")

            for i in range(5):
                priority_heap.insert(i * 10)
            print(f"Heap after insertions: {priority_heap.display()}")
            print(f"Extracted min from heap: {priority_heap.extract_min()}")
    except ValueError:
        print("Invalid input. Please enter a valid number.")
