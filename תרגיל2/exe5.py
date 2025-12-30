# כתבי פונקציה partition שמחלקת את מערך לשלושה קטעים תוך שימוש בשני pivot-ים
def dual_pivot_partition(a, key):
    if len(a) < 2:
        return 0, len(a) - 1  # לא ניתן לחלק מערך עם פחות משני איברים

    # בוחרים שני פיבוטים
    if key(a[0]) > key(a[-1]):
        a[0], a[-1] = a[-1], a[0]

    pivot1 = a[0]
    pivot2 = a[-1]
    pivot1_key = key(pivot1)
    pivot2_key = key(pivot2)

    lt = 1  # אינדקס לאיברים קטנים מהפיבוט הראשון
    gt = len(a) - 2  # אינדקס לאיברים גדולים מהפיבוט השני
    i = 1   # אינדקס לסריקה

    while i <= gt:
        if key(a[i]) < pivot1_key:
            a[i], a[lt] = a[lt], a[i]
            lt += 1
            i += 1
        elif key(a[i]) > pivot2_key:
            a[i], a[gt] = a[gt], a[i]
            gt -= 1
        else:
            i += 1

    # מחזירים את הפיבוטים למקומם הסופי
    a[0], a[lt - 1] = a[lt - 1], a[0]
    a[-1], a[gt + 1] = a[gt + 1], a[-1]

    return lt - 1, gt + 1  # מחזירים את האינדקסים של שני הפיבוטים           