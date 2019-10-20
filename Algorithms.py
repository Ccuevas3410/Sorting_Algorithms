def selectionSort(A):
    comparisons = 0
    swaps = 0
    global index
    global SWAPSalgo

    for i in range(len(A)):

        # Find the minimum element in remaining
        # unsorted array
        min_idx = i
        for j in range(i + 1, len(A)):
            if A[min_idx] > A[j]:
                min_idx = j
                comparisons += 1
                # Swap the found minimum element with
        # the first element
        A[i], A[min_idx] = A[min_idx], A[i]
        swaps += 1




def insertionSort(arr):
    # Traverse through 1 to len(arr)
    comparisons = 0
    swaps = 0
    global index
    global SWAPSalgo

    for i in range(1, len(arr)):
        key = arr[i]

        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i - 1
        while j >= 0 and key < arr[j]:
            comparisons += 1
            if key < arr[j]:
                comparisons += 1

                arr[j + 1] = arr[j]
                swaps += 1
                j -= 1
                arr[j + 1] = key
                swaps += 1



def partition(arr, low, high):
    index = (low - 1)  # index of smaller element
    pivot = arr[high]  # pivot

    for j in range(low, high):

        # If current element is smaller than or
        # equal to pivot
        if arr[j] <= pivot:
            # increment index of smaller element
            index = index + 1
            arr[index], arr[j] = arr[j], arr[index]

    arr[index + 1], arr[high] = arr[high], arr[index + 1]
    return (index + 1)

# Function to do Quick sort
def quickSort(arr, low, high):

    comparisons = 0
    swaps = 0

    if low < high:
        # pi is partitioning index, arr[p] is now
        # at right place
        pi = partition(arr, low, high)

        # Separately sort elements before
        # partition and after partition
        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)





def bubbleSort(nums):


    comparisons = 0
    swaps = 0
    global index
    global SWAPSalgo

    swapped = True
    while swapped:
        swapped = False
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                comparisons+=1
                # Swap the elements
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                swaps +=1
                # Set the flag to True so we'll loop again
                swapped = True

    SWAPSalgo[index] = {'bubbleSort': swaps}
    index += 1
    print("Insertion Sort: The # of comparisons: ", comparisons, ", and the # of SWAPS is: ", swaps)



def left(i):
    return 2 * i + 1


# find right child of node i
def right(i):
    return 2 * i + 2


# calculate and return array size
def heapSize(A):
    return len(A) - 1


# This fuction takes an array and Heapyfies
# the at node i
def MaxHeapify(A, i):
    # print("in heapy", i)
    l = left(i)
    r = right(i)

    # heapSize = len(A)
    # print("left", l, "Rightt", r, "Size", heapSize)
    if l <= heapSize(A) and A[l] > A[i]:
        largest = l
    else:
        largest = i
    if r <= heapSize(A) and A[r] > A[largest]:
        largest = r
    if largest != i:
        # print("Largest", largest)
        A[i], A[largest] = A[largest], A[i]
        # print("List", A)
        MaxHeapify(A, largest)

    # this function makes a heapified array


def BuildMaxHeap(A):
    for i in range(int(heapSize(A) / 2) - 1, -1, -1):
        MaxHeapify(A, i)

    # Sorting is done using heap of array


def HeapSort(A):
    BuildMaxHeap(A)
    B = list()
    heapSize1 = heapSize(A)
    for i in range(heapSize(A), 0, -1):
        A[0], A[i] = A[i], A[0]
        B.append(A[heapSize1])
        A = A[:-1]
        heapSize1 = heapSize1 - 1
        MaxHeapify(A, 0)

    # randomly generates list of different

