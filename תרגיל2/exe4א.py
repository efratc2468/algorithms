def lomuto_partition(a, key):
    pivot = a[-1]                 # בוחרים את האיבר האחרון כפיבוט
    pivot_key = key(pivot)
    i = -1                        # מצביע שמתקדם עם מציאת איברים קטנים מה-pivot

    for j in range(len(a) - 1):   # עוברים על כל האיברים חוץ מהאחרון
        if key(a[j]) <= pivot_key:
            i += 1
            a[i], a[j] = a[j], a[i]

    # מציבים את הפיבוט במקומו הסופי
    a[i + 1], a[-1] = a[-1], a[i + 1]

    return i + 1                  # מחזירים את אינדקס ה-pivot לאחר ההחלפה
# דוגמה לשימוש בפונקציה
if __name__ == "__main__":  
    arr = [3, 6, 8, 10, 1, 2, 1]
    pivot_index = lomuto_partition(arr, key=lambda x: x)
    print("Pivot index:", pivot_index)  # Output: Pivot index: (index of the pivot after partitioning)
    print("Partitioned array:", arr)    # Output: Partitioned array: (array with elements <= pivot on the left and > pivot on the right)