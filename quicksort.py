#Sort a given set of n integer elements using Quick Sort method and compute its time complexity. 
#Run the program for varied values of n> 5000, and record the time taken to sort.

import time
from numpy.random import randint

#function to sort the array using pivot element
def partition(array,low,high):
    pivot=array[high]
    i=low-1
    for j in range(low,high):
        if array[j]<=pivot:
            i=i+1
            (array[i],array[j])=(array[j],array[i])
    (array[i+1],array[high])=(array[high],array[i+1])
    return i+1

#Quicksort algorithm
def quicksort(array,low,high):
    if low<high:
        pi=partition(array,low,high)
        quicksort(array,low,pi-1)
        quicksort(array,pi+1,high)

#user input
n = int(input("Enter the number of elements: "))
array = []
for i in range(n):
    array.append(int(input(f"Enter element {i+1}: ")))
quicksort(array,0,len(array)-1)
print("The sorted array is:", array)

#random input
print("****************RUNNING TIME ANALYSIS FOR RANDOM INPUT********************")
y=1
while y:
    i=int(input("Enter a large number above 5000:"))
    array=randint(0,i,i)  #Making an array of random integers of size 1000*i
    start_time = time.time()   #records the time just before mergesort is implimented
    quicksort(array,0,len(array)-1)
    end_time = time.time()   #records the time just after mergesort is implimented
    print("The time taken to sort",len(array),"elements is", end_time - start_time,"seconds")
    y=int(input("Do you want to continue?(1/0):"))