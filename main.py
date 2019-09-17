import pandas as pd
import seaborn as sns
import numpy as no
import matplotlib.pyplot as plt
import time
from time import perf_counter
import csv
import timeit

def selectionSort(A):

    comparisons = 0
    swaps = 0

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

    print("Selection Sort: The # of comparisons: ", comparisons, ", and the # of SWAPS is: ", swaps)



def insertionSort(arr):
    # Traverse through 1 to len(arr)
    comparisons = 0
    swaps = 0

    for i in range(1, len(arr)):

        key = arr[i]

        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i - 1
        while j >= 0 and key < arr[j]:
            comparisons += 1
            arr[j + 1] = arr[j]
            swaps+=1
            j -= 1
        arr[j + 1] = key
        swaps += 1
    print("Insertion Sort: The # of comparisons: ", comparisons, ", and the # of SWAPS is: ", swaps)


def partition(arr, low, high):
    i = (low - 1)  # index of smaller element
    pivot = arr[high]  # pivot

    for j in range(low, high):

        # If current element is smaller than or
        # equal to pivot
        if arr[j] <= pivot:
            # increment index of smaller element
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return (i + 1)




# Function to do Quick sort
def quickSort(arr, low, high):



    comparisons=0
    swaps = 0

    if low < high:
         # pi is partitioning index, arr[p] is now
        # at right place
        pi = partition(arr, low, high)

        # Separately sort elements before
        # partition and after partition
        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)





def main():


 arr=[0]
 for i in range(1000000, 1,-1):
    arr.append(i)
 length=len(arr)





 t1_start = perf_counter()
 selectionSort(arr[:])
 t1_stop = perf_counter()
 timer=  (t1_stop-t1_start/100000)
 print("Elapsed time during Selection Sort:",timer)




 t1_start = perf_counter()
 insertionSort(arr[:])
 t1_stop = perf_counter()
 timer=  (t1_stop-t1_start/100000)
 print("Elapsed time during Selection Sort:",timer)






if __name__ == '__main__':
    main()