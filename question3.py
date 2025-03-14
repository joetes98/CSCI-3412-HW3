def isSorted(arr): # check if array is sorted in ascending order
    for i in range(1, len(arr)):
        if arr[i-1] > arr[i]:
            return False
    return True

# optimized version of bubblesort
def bubbleSort(arr):
    n = len(arr) - 1
    swapped = False

    # loop while list in unsorted, last pass will not swap any elements and swapped == True
    while not swapped:
        newn = 0
        swapped = True
        for i in range(0, n):
            if arr[i] > arr[i+1]:
                swapped = False
                arr[i], arr[i+1] = arr[i+1], arr[i]
                newn = i # all elements after the last swap are sorted, do not need to be checked again
        n = newn

def partition(arr, low, high):
    i = low - 1  # smaller element position
    pivot = arr[high]  # pivot element
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return (i+1)

def quickSort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quickSort(arr, low, pi-1)
        quickSort(arr, pi+1, high)

def main():

    print("1. Bubble Sort\n2. Quick Sort")
    choice = input()

    # test optimized bubbleSort
    if int(choice) == 1:
        with open("rand1000.txt", 'r') as file:
            nums = file.read().split()

            integers = [int(num) for num in nums]

        print("Bubble Sort")
        bubbleSort(integers)
        print(integers)
        print(isSorted(integers))

    # test quickSort
    elif int(choice) == 2:
        with open("rand1000.txt", 'r') as file:
            nums = file.read().split()

            integers = [int(num) for num in nums]

        print("Quick Sort")
        length = len(integers) - 1
        quickSort(integers, 0, length)
        print(integers)
        print(isSorted(integers))

    else:
        print("Not a choice")

if __name__ == '__main__':
    main()