#פונקציה lists_sorted_merge מיון של רשימות 

def merge_sorted_lists( lists, key):
    merged_list = []
    indices = [0] * len(lists)

    while True:
        min_value = None
        min_list_index = -1

        for i in range(len(lists)):
            if indices[i] < len(lists[i]):
                current_value = lists[i][indices[i]]
                if min_value is None or key(current_value) < key(min_value):
                    min_value = current_value
                    min_list_index = i

        if min_list_index == -1:
            break

        merged_list.append(min_value)
        indices[min_list_index] += 1

    return merged_list
# דוגמה לשימוש בפונקציה
if __name__ == "__main__":
    list1 = [1, 4, 7]
    list2 = [2, 5, 8]
    list3 = [3, 6, 9]

    merged = merge_sorted_lists([list1, list2, list3], key=lambda x: x)
    print(merged)  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]# הפונקציה מקבלת רשימה של רשימות ממוינות ופונקציית מפתח ומחזירה רשימה ממוינת מאוחדת.    
    #מה הסיבוכיות של הפונקציה?
    # הסיבוכיות של הפונקציה היא O(N log k), כאשר N הוא סך כל האלמנטים בכל הרשימות ו-k הוא מספר הרשימות.