def min_find(a, key):
    if not a:
        return None, None

    min_item = a[0]
    max_item = a[0]

    for item in a[1:]:
        if key(item) < key(min_item):
            min_item = item
        if key(item) > key(max_item):
            max_item = item

    return min_item, max_item
