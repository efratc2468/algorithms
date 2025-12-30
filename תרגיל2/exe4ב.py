def hoare_partition(a, key):
    pivot = a[0]
    pivot_key = key(pivot)

    i = -1
    j = len(a)

    while True:
        # זזים קדימה עד שימצא איבר שלא קטן מהפיבוט
        i += 1
        while key(a[i]) < pivot_key:
            i += 1

        # זזים אחורה עד שימצא איבר שלא גדול מהפיבוט
        j -= 1
        while key(a[j]) > pivot_key:
            j -= 1

        # אם עברו אחד את השני – מחזירים את נקודת החלוקה
        if i >= j:
            return j

        # אם עדיין לא עברו – מחליפים בין האיברים
        a[i], a[j] = a[j], a[i]

# 4ג//Lomuto הפיבוט מגיע למקומו הסופי במערך
#4ד//o(n) 