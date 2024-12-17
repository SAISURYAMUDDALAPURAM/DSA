#sort elements : Arrange elements of array into ascending order
arr=[6,5,43,3,2,1]
n=len(arr)

for i in range(0,n-1):
    for j in range(0,n-1):
        if arr[j]>arr[j+1]:
            temp=arr[j+1]
            arr[j+1]=arr[j]
            arr[j]=temp
        
print(arr)

#selection sort : Select the Minimum in entire array and Swap it 

arr=[6,5,-4,3,0,-1]
n=len(arr)
for i in range(n-1):
    min_index=i
    for j in range(i,n):
        if arr[j]<arr[min_index]:
            min_index=j
    temp=arr[i]
    arr[i]=arr[min_index]
    arr[min_index]=temp
print(arr)


#bubble sort : Push the maximum to the last by adjacent swapping /swaps
arr=[1,2,3]
n=len(arr)
for i in range(n-1):
    swap=0
    for j in range(n-i-1):
        if arr[j]>arr[j+1]:
            temp=arr[j+1]
            arr[j+1]=arr[j]
            arr[j]=temp
            swap=1
    if swap==0:
        break
    print("runs")
print(arr)


#insertion sort : Takes an Element and Places it in Correct position 

arr=[4,3,2,1]
n=len(arr)

for i in range(n):
    j=i
    while(j>0 and arr[j]<arr[j-1]):
        temp=arr[j]
        arr[j]=arr[j-1]
        arr[j-1]=temp
        j-=1

print(arr)
