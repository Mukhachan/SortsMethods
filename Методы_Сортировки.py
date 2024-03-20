# Сортировка пузырьком
def bubbleSort(arr):
    flag = True
    for j in range(1, len(arr)):
        a = arr[j-1]
        b = arr[j]
        if b<a:
            flag = False
            arr[j-1], arr[j] = arr[j], arr[j-1]
    
    if flag == False: return bubbleSort(arr)
    return arr


# Сортировка выбором
def selectionSort(array: list): 
    for i in range(len(array)-1):
        min_idx = i 
        for idx in range(i+1, len(array)-1):
            if array[idx] < array[min_idx]:
                min_idx = idx
        array[i], array[min_idx] = array[min_idx], array[i]
    
    return array


# Сортировка вставкой
def insertSort(array: list):
    for i in range(1, len(array)):
        x = array[i]
        j = i
        
        while j > 0 and array[j-1] > x:
            array[j] = array[j-1]
            j-=1
        array[j]=x
    
    return array    
    
# Сортировка кучей
def heapify(array: list, n, i):
    largest = i
    l = 2*i+1
    r = 2*i+2
    
    if l<n and array[i] < array[l]: largest = l
    if r<n and array[largest] < array[r]: largest = r
    if largest != i:
        array[i], array[largest] = array[largest], array[i]
        heapify(array, n, largest)
def heapSort(array: list):
    for i in range(len(array)//2, -1, -1):
        heapify(array, len(array), i)
    for i in range(len(array)-1, 0, -1):
        array[i], array[0] = array[0], array[i]
        heapify(array, i, 0)
    return array

# Сортировка слиянием (не работает... хз почему)
def mergeSort(nums):
    if len(nums)==1: 
        return nums
    mid = (len(nums)-1)//2
    lst1 = mergeSort(nums[:mid+1])
    lst2 = mergeSort(nums[mid+1:])
    result = merge(lst1, lst2)    
    return result
def merge(lst1, lst2):
    lst = []
    i, j = 0, 0
    while i<=len(lst1)-1 and j<=len(lst2)-1:
        if lst1[i]<lst2[j]:
            lst.append(lst1[i])
            i+=1 
        else:
            lst.append(lst2[j])
            j+=1
    
    if i>len(lst1)-1:
        while i<=len(lst2)-1:
            lst.append(lst2[j])
            j+=1
    else:
        while i<=len(lst1)-1:
            lst.append(lst1[i])
            i+=1
    return lst
 
# Быстрая Сортировка (реально быстрая)
def quickSort(array: list):
    if len(array) > 1:
        pivot = array.pop()
        grtr_lst, equal_lst, smlr_lst = [], [pivot], []
        for item in array:
            if item == pivot: equal_lst.append(item)
            elif item > pivot: grtr_lst.append(item)
            else: smlr_lst.append(item)
        return quickSort(smlr_lst) + equal_lst + quickSort(grtr_lst)
    else:
        return array
        
array = [4,1,3,2,5,8,7,9,10]

print("Сортировка пузырьком:", bubbleSort(array))
print("Сортировка выбором:", selectionSort(array))
print("Сортировка вставкой:", insertSort(array))
print("Сортировка кучей:", heapSort(array))
print("Сортировка слиянием:", mergeSort(array))
print("Быстрая Сортировка:", quickSort(array))


