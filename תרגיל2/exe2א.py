def sorted_is(a, key=lambda x: x):
    for i in range(len(a) - 1):
        if key(a[i]) > key(a[i + 1]):
            return False
    return True
