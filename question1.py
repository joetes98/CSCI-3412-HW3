import time

def max_heapify_recursive(array, i):
    left = 2 * i
    right = 2 * i + 1
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
        left = 2 * i
        right = 2 * i + 1
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
        
def build_max_heap_recursive(array):
    for i in reversed(range(len(array)//2)):
        max_heapify_recursive(array, i)

def build_max_heap_iterative(array):
    for i in reversed(range(len(array)//2)):
        max_heapify_iterative(array, i)

def timeEfficiency(funcName, *args, **kwargs):
    # record start time
    startTime = time.time()

    # func = funcName(*args)

    # record end time
    endTime = time.time()
    timeEfficiency = endTime - startTime

    print(f"Start time: {startTime}")
    print(f"End Time: {endTime}")
    print(f"Total time: {timeEfficiency}")

    # return startTime, endTime, timeEfficiency

def main():
    
    print("1: Recursive\n2: Iterative")
    choice = input()

    if int(choice) == 1:
        with open("rand1000000.txt", 'r') as file:
            nums = file.read().split()

            integers = [int(num) for num in nums]
    
        timeEfficiency(build_max_heap_recursive, integers)

    elif int(choice) == 2:
        with open("rand1000000.txt", 'r') as file:
            nums = file.read().split()

            integers = [int(num) for num in nums]
    
        timeEfficiency(build_max_heap_iterative, integers)
    
if __name__ == '__main__':
    main()