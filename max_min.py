#python program to find maximum and minimum values in an array
#using divide and conquor method

#function to recursively find max and min values
def find_min_max(arr, low, high):
    if low == high:
        return arr[low], arr[high]
    mid = (low + high) // 2
    min_left, max_left = find_min_max(arr, low, mid)
    min_right, max_right = find_min_max(arr, mid + 1, high)
    return min(min_left, min_right), max(max_left, max_right)

#providing input
n = int(input("Enter the number of elements: "))
arr = []
for i in range(n):
    a=int(input(f"Enter element {i+1}: "))
    arr.append(a)
min_value, max_value = find_min_max(arr, 0, n - 1)
print("The minimum value is:", min_value)
print("The maximum value is:", max_value)