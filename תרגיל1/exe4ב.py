from תרגיל1.random_tuples import create_random_tuples


def min_find(a, key):
    if not a:
        return None

    min_item = a[0]
    min_key = key(a[0])

    for item in a[1:]:
        k = key(item)
        if k < min_key:
            min_key = k
            min_item = item

    return min_item

def max_find(a, key):
    if not a:
        return None

    max_item = a[0]
    max_key = key(a[0])

    for item in a[1:]:
        k = key(item)
        if k > max_key:
            max_key = k
            max_item = item

    return max_item


data = create_random_tuples(100, 3, [str, float, int])

mn = min_find(data, key=lambda x: x[2])
mx = max_find(data, key=lambda x: x[2])

print("min=", mn[2])
print("max=", mx[2])
