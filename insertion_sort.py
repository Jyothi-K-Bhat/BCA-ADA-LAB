#Write a program to sort a list of N elements using Insertion Sort Technique.

#Insertion sort function
def insertion_sort(list):
    for i in range(1, len(list)):
        key = list[i]
        j = i - 1
        while j >= 0 and list[j] > key:
            list[j + 1] = list[j]
            j -= 1
        list[j + 1] = key

#reading input
n=int(input("Enter the number of elements:"))
list = []
print("Enter the elements:")
for i in range(n):
    a=int(input())
    list.append(a)
insertion_sort(list)
print(list)