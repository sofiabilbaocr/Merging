'''
Merge Sort implementation (Divide and Conquer)
'''

from memory_profiler import profile

def merge(left: list, right: list) -> list:
    #Función auxiliar para combinar dos listas ordenadas
    merged = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    #Agrega los elementos restantes
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged

@profile
def merge_sort(arr: list) -> list:
    #Función principal recursiva de Merge Sort.
    if len(arr) <= 1:
        return arr

    #Divide
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    #Conquest
    return merge(left_half, right_half)

if __name__ == '__main__':
    test_arr = [33, 14, 55, 1, 3]
    #merge_sort devuelve una nueva lista, no modifica la original in-place
    sorted_arr = merge_sort(test_arr.copy())
    print(f'Unsorted arr: {test_arr}')
    print(f'Sorted arr: {sorted_arr}')