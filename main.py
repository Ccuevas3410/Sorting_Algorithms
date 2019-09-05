import pandas as pd
import seaborn as sns
import numpy as no
import matplotlib.pyplot as plt
import time
from time import perf_counter
import csv


def selection_sort(arr):

    comparisons = 0
    swaps = 0

    for i in range(len(arr)):

        # Find the minimum element in remaining
        # unsorted array
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j
                comparisons+=1

        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        swaps+=1


    print("The # of comparisons: ", comparisons, ", and the # of SWAPS is: ",swaps)
    print(arr)

def insertion_sort(arr):
    swaps=0
    comparisons=0

    for i in range(len(arr)):
        less = True
        j=i
    while j> 0 and less:
        if (arr[j]<arr[j-1]):
            dummy=arr[j-1]
            arr[j-1]= arr[j]
            arr[j]=dummy
            j=-1

            swaps+=1
            comparisons+=1

        else:
            less=False

        comparisons+=1

    for j in range(len(arr)):
        print(arr)


def main():

 test=0
 for i in range(1000000):
    test+=i
    print(i)

 t1_start = perf_counter()
 selection_sort(test)
 t1_stop = perf_counter()
 timer=  (t1_stop-t1_start)
 print("Elapsed time during the whole program in seconds:",timer)
 print("{:.10f}".format(timer))

 arr = [2, 3, 1, 5]
 arrTwo = [10, 2, 3, 5]

 with open('mycsv.csv', 'w', newline='') as data:
     thewriter = csv.writer(data)

     thewriter.writerow(['Time', 'Swaps', 'Comparisons'])
     thewriter.writerow(['Selection Sort', 'Insertion Sort', 'COL3'])

 for i in range(len(arr)):
     print(arr[i])

if __name__ == '__main__':
    main()