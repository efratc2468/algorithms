#tar3
def parent(i):
    return (i - 1) // 2

def left(i):
    return 2 * i + 1

def right(i):
    return 2 * i + 2
#tar4
def is_max_heap(arr, i=0, key=lambda x: x):
    n = len(arr)

    for child in range(i + 1, n):
        p = (child - 1) // 2   

        if key(arr[p]) < key(arr[child]):
            return False

    return True
#tar5
def max_heapify(arr, i, heap_size, key=lambda x: x):
  

    left = 2 * i + 1
    right = 2 * i + 2
    largest = i

    # בדיקה מול הבן השמאלי
    if left < heap_size and key(arr[left]) > key(arr[largest]):
        largest = left

    # בדיקה מול הבן הימני
    if right < heap_size and key(arr[right]) > key(arr[largest]):
        largest = right

    # אם אחד הילדים גדול יותר – מחליפים וממשיכים לרדת
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        max_heapify(arr, largest, heap_size, key)


#tar6
def build_max_heap(arr, key=lambda x: x):
    

    n = len(arr)

    # מתחילים מהאיבר האחרון שיש לו ילדים ומטפסים עד השורש
    for i in range(n // 2 - 1, -1, -1):
        max_heapify(arr, i, n, key)

#tar7
def heap_sort(arr, key=lambda x: x):
  

    n = len(arr)

    #  בניית ערימת מקסימום
    build_max_heap(arr, key)

    #  הוצאה חוזרת של האיבר הגדול ביותר
    for end in range(n - 1, 0, -1):
        # החלפת השורש (הגדול ביותר) עם האיבר האחרון
        arr[0], arr[end] = arr[end], arr[0]

        # תיקון הערימה בטווח שנותר
        max_heapify(arr, 0, end, key)
#tar8
