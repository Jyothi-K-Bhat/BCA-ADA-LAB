#Write a program to sort a list of N elements using Selection Sort Technique.

#function to selectively sort an array 
def selection_sort(list):
    for i in range(len(list)):
        min_index=i
        for j in range(i+1,len(list)):
            if list[j] < list[min_index]:
                min_index = j
    list[i], list[min_index] = list[min_index], list[i]

#reading input
n=int(input("Enter the number of elements:"))
list = []
print("Enter the elements:")
for i in range(n):
    a=int(input())
    list.append(a)
selection_sort(list)
print(list)