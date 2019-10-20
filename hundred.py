

import pandas as pd
import seaborn as sns
import numpy as np
from time import perf_counter
import time
from numpy.random import seed
from numpy.random import randint
import matplotlib.pyplot as plt
import Algorithms as algo

# HEAPSORT

elements = list()
times = list()
for i in range(1, 10):
    # generate some integers
    a = randint(0, 100 * i, 100 * i)
    # print(i)
    start = time.perf_counter()
    algo.HeapSort(a[:])
    end = time.perf_counter()
    # print("Sorted list is ", a)
    print(len(a), "Elements Sorted by HeapSort in ", end - start)
    elements.append(len(a))
    times.append(end - start)

plt.plot(elements, times,'r', label='Heap Sort')




# INSERTION SORT
elements = list()
times = list()
for i in range(1, 10):
    # generate some integers
    a = randint(0, 100 * i, 100 * i)
    # print(i)
    start = time.perf_counter()
    algo.insertionSort(a[:])
    end = time.perf_counter()
    # print("Sorted list is ", a)
    print(len(a), "Elements Sorted by Insertion Sort in ", end - start)
    elements.append(len(a))
    times.append(end - start)
plt.plot(elements, times,'b', label='Insertion Sort')



# SELECTION SORT
elements = list()
times = list()
for i in range(1, 10):
    # generate some integers
    a = randint(0, 100 * i, 100 * i)
    # print(i)
    start = time.perf_counter()
    algo.selectionSort(a[:])
    end = time.perf_counter()
    # print("Sorted list is ", a)
    print(len(a), "Elements Sorted by Selection Sort in ", end - start)
    elements.append(len(a))
    times.append(end - start)

plt.plot(elements, times,'y', label='Selection Sort')


#QUICKSORT
elements = list()
times = list()
for i in range(1, 10):
    # generate some integers
    a = randint(0, 100 * i, 100 * i)
    # print(i)
    start = time.perf_counter()
    algo.quickSort(a[:],0,99)
    end = time.perf_counter()
    # print("Sorted list is ", a)
    print(len(a), "Elements Sorted by Quick Sort in ", end - start)
    elements.append(len(a))
    times.append(end - start)

plt.plot(elements, times,'g', label='Quick Sort')
plt.xlabel('List Length')
plt.ylabel('Time Complexity')
plt.title('100 Element array')

plt.grid()
plt.legend()
plt.show()

