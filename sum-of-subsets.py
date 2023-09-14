def isSubsetSum(set, n, sum):
    if sum == 0:
        return True
    if n==0:
        return False
    if set[n - 1] > sum:
        return isSubsetSum(set, n - 1, sum)
    else:
        return isSubsetSum(set, n - 1, sum) or isSubsetSum(set, n - 1, sum - set[n - 1])
def findSubsetSum(set, n, sum,total):
    if not isSubsetSum(set, n, sum):
        total=None
    for j in range(n-1,-1,-1):
        subset=[]
        i = j
        temp=sum
        while temp != 0 and i >= 0:
            if set[i] <= temp:
                subset.append(set[i])
                temp-=set[i]
            i-=1
        if temp==0:
            total.append(subset)
n=int(input("Enter the number of elements:"))
set = []
for i in range(n):
    set.append(int(input(f"Enter the {i+1} element:")))
sum=int(input("Enter the sum:"))
total = []
findSubsetSum(set, len(set), sum, total)
if total is not None:
    print(total)
else:
    print("No subset with sum exists.")