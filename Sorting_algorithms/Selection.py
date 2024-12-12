arr=[9,65,78,43,23,11,56,11,10,13,18]
n=len(arr)
for i in range(n):
    min_index=i
    for j in range(i + 1,n):
        if arr[min_index]>arr[j]:
            min_index=j
    arr[min_index],arr[i]=arr[i],arr[min_index]
print("sorted array is:-",arr)


