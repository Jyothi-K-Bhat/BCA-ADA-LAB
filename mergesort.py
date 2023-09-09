#Sort a given set of n integer elements using Merge Sort method and compute its time complexity. 
#Run the program for varied values of n> 5000, and record the time taken to sort.

import time
from numpy.random import randint

#function to split and merge the array
def mergesort(array):
    if len(array)>1:
        r=len(array)//2
        left=array[:r]
        right=array[r:]
        mergesort(left)
        mergesort(right)
        i,j,k=0,0,0
        while i<len(left) and j<len(right):
            if left[i]<right[j]:
                array[k]=left[i]
                i+=1
            else:
                array[k]=right[j]
                j+=1
            k+=1
        while i<len(left):
            array[k]=left[i]
            i+=1
            k+=1
        while j<len(right):
            array[k]=right[j]
            j+=1
            k+=1

#user input
n = int(input("Enter the number of elements: "))
array = []
for i in range(n):
    array.append(int(input(f"Enter element {i+1}: ")))
mergesort(array)
print("The sorted array is:", array)

#random input
print("****************RUNNING TIME ANALYSIS FOR RANDOM INPUT********************")
for i in range(5,10):
    array=randint(0,1000*i,1000*i)  #Making an array of random integers of size 1000*i
    start_time = time.time()   #records the time just before mergesort is implimented
    mergesort(array)
    end_time = time.time()   #records the time just after mergesort is implimented
    print("The time taken to sort",len(array),"elements is", end_time - start_time,"seconds")
