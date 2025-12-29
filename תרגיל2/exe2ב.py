from תרגיל2.exe2א import sorted_is


def merge(a, b, key=lambda x: x):
    
    if not sorted_is(a, key) or not sorted_is(b, key):
        return None

    result = []
    i = j = 0

    
    while i < len(a) and j < len(b):
        if key(a[i]) <= key(b[j]):
            result.append(a[i])
            i += 1
        else:
            result.append(b[j])
            j += 1

    
    result.extend(a[i:])
    result.extend(b[j:])

    return result
