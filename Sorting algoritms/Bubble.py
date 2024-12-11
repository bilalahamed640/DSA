def bubble_sort():
    arr=[7,8,4,5,2,0,1,78,56,65,34,43,23,12]
    n=len(arr)
    for i in range(n-1):
        swapped=False
        for j in range(n-i-1):
           if arr[j+1]<arr[j]:
               arr[j],arr[j+1]=arr[j+1],arr[j]
               swapped=True
        if not swapped:
            break
    print("Sorted array=",arr)
bubble_sort()
