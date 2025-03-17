import time

def max_heapify_recursive(array, i):
    left = 2 * i + 1
    right = 2 * i + 2
    length = len(array) - 1  # for termination condition \
    largest = i

    if left <= length and array[i] < array[left]:
        largest = left
        
    if right <= length and array[largest] < array[right]:
        largest = right

    if largest != i:
        array[i], array[largest] = array[largest], array[i]
        max_heapify_recursive(array, largest)   # largest == new i

def max_heapify_iterative(array, i):
    while 1:
        left = 2 * i + 1
        right = 2 * i + 2
        length = len(array) - 1  # for termination condition \
        largest = i

        if left <= length and array[i] < array[left]:
            largest = left

        if right <= length and array[largest] < array[right]:
            largest = right
            
        if largest != i:
            array[i], array[largest] = array[largest], array[i]
            i = largest # largest  == new i

        else:
            break

def is_max_heap(arr):
    n = len(arr)
    
    # check all but leaf nodes nodes
    for i in range(n // 2):
        left = 2 * i + 1
        right = 2 * i + 2
        
        # check if max heap condition is violated for left child
        if left < n and arr[i] < arr[left]:
            return False
        
        # check if max heap condition is violated for right child
        if right < n and arr[i] < arr[right]:
            return False
    
    return True
        
def build_max_heap_recursive(array):
    for i in reversed(range(len(array)//2)):
        max_heapify_recursive(array, i)

def build_max_heap_iterative(array):
    for i in reversed(range(len(array)//2)):
        max_heapify_iterative(array, i)

def main():
    
    print("1: Recursive\n2: Iterative")
    choice = input()

    # Build Max Heap Recursive Version
    if int(choice) == 1:
        with open("rand1000000.txt", 'r') as file:
            nums = file.read().split()

            integers = [int(num) for num in nums]

        startTime = time.time()
        build_max_heap_recursive(integers)
        endTime = time.time()
        totalTime = endTime - startTime

        print("Start Time: ", startTime)
        print("End Time: ", endTime)
        print("Total Time: ", totalTime)

        if is_max_heap(integers):
            print("The array is a max-heap.")
        else:
            print("The array is not a max-heap.")

    # Build Max Heap Iterative Version
    elif int(choice) == 2:
        with open("rand1000000.txt", 'r') as file:
            nums = file.read().split()

            integers = [int(num) for num in nums]
    
        startTime = time.time()
        build_max_heap_iterative(integers)
        endTime = time.time()
        totalTime = endTime - startTime

        print("Start Time: ", startTime)
        print("End Time: ", endTime)
        print("Total Time: ", totalTime)

        if is_max_heap(integers):
            print("The array is a max-heap.")
        else:
            print("The array is not a max-heap.")
    
if __name__ == '__main__':
    main()