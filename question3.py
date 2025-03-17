import time
import matplotlib.pyplot as plt

def isSorted(arr): # check if array is sorted in ascending order
    for i in range(1, len(arr)):
        if arr[i-1] > arr[i]:
            return False
    return True

# optimized version of bubblesort
def bubbleSort(arr, low, high):
    '''
    The low and high indices are included for the modified Quick Sort. 
    
    In the modified Quick Sort, we call bubble sort if the subarray is less than a given value.
    We need to specify the indices of the  partition for bubble sort, since the modified quick sort
    takes in the entire array as a parameter.
    
    '''
    swapped = False

    # loop while list in unsorted, last pass will not swap any elements and swapped == True
    while not swapped:
        newn = 0
        swapped = True
        for i in range(low, high):
            if arr[i] > arr[i+1]:
                swapped = False
                arr[i], arr[i+1] = arr[i+1], arr[i]
                newn = i # all elements after the last swap are sorted, do not need to be checked again
        high = newn

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


def modifiedQuickSort(arr, low, high, k):
    '''
    This version of quick sort will call the optimized bubble sort
    if the length of the subarray is less than or equal to a given value k.
    '''
    if low < high:
        # bubble Sort if less then k value
        if (high - low + 1) <= k:
            bubbleSort(arr, low, high)
        else:
            # recursive call modifiedQuickSort
            pi = partition(arr, low, high)
            modifiedQuickSort(arr, low, pi-1, k)
            modifiedQuickSort(arr, pi+1, high, k)

def main():

    print("1. Bubble Sort\n2. Quick Sort\n3. Modified Quick Sort\n4. Modified Quick Sort Optimal K")
    choice = input()

    # test optimized bubbleSort
    if int(choice) == 1:
        with open("rand1000.txt", 'r') as file:
            nums = file.read().split()

            integers = [int(num) for num in nums]

        print("Bubble Sort")
        length = len(integers) - 1
        bubbleSort(integers, 0, length)
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



    # test modifiedQuickSort
    elif int(choice) == 3:
        with open("rand1000.txt", 'r') as file:
            nums = file.read().split()

            integers = [int(num) for num in nums]
        
        print("Modified Quick Sort")
        length = len(integers) - 1
        modifiedQuickSort(integers, 0, length, 10)
        print(integers)
        print(isSorted(integers))



    elif int(choice) == 4:       
        k_values = []
        const = 5
        
        # Run modified Quick sort for k: 2-22
        for k in range(2, 23):
            kTime = 0
            # run each k value 20 times
            for i in range(const):
                with open("rand1000000.txt", 'r') as file:
                    nums = file.read().split()

                    integers = [int(num) for num in nums]
                length = len(integers) - 1
                # record start time
                startTime = time.time()
                modifiedQuickSort(integers, 0, length, k)
                #record end time
                endTime = time.time()
                # compute total sorting time
                totalTime = endTime - startTime
                kTime += totalTime
            # find the average total sorting time for each k value
            avg = kTime/const
            k_values.append(avg)
        
        print(k_values)
        # Find the minimum k-value
        minimum = min(k_values)
        minPos = k_values.index(minimum)
        print("Optimal K Value: ", minPos + 2)

        xValues  = [k for k in range(2,23)]

        # diplay data in line graph
        plt.plot(xValues, k_values)
        plt.xlabel('K value')
        plt.ylabel('Time (Seconds)')
        plt.xticks(xValues)
        plt.title('Optimal K Value')
        plt.show()

    else:
        print("Not a choice")

if __name__ == '__main__':
    main()