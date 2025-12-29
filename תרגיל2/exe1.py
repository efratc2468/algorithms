from random_tuples import create_random_tuples

# יצירת רשימה של tuples: (str, float, int)
tuples_list = create_random_tuples(10, 3, [str, float, int])

print("הרשימה המקורית:")
for t in tuples_list:
    print(t)

sorted_by_str = sorted(tuples_list, key=lambda x: x[0])

print("\nמיון לפי הרכיב הראשון (str):")
for t in sorted_by_str:
    print(t)

sorted_by_float = sorted(tuples_list, key=lambda x: x[1])

print("\nמיון לפי הרכיב השני (float):")
for t in sorted_by_float:
    print(t)

sorted_by_int = sorted(tuples_list, key=lambda x: x[2])

print("\nמיון לפי הרכיב השלישי (int):")
for t in sorted_by_int:
    print(t)
