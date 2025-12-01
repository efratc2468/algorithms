from random_tuples import create_random_tuples

def sort_insertion(a, key):
    n = len(a)

    for i in range(1, n):
        current = a[i]
        j = i - 1

        while j >= 0 and key(a[j]) > key(current):
            a[j + 1] = a[j]
            j -= 1

        a[j + 1] = current


def main():
    list1 = create_random_tuples(10, 3, [str, float, int])
    sort_insertion(list1, key=lambda x: x[0])

    print("Sorted by item 0 (string):")
    for t in list1:
        print(t)

    list2 = create_random_tuples(10, 3, [str, float, int])
    sort_insertion(list2, key=lambda x: x[1])

    print("Sorted by item 1 (float):")
    for t in list2:
        print(t)

    list3 = create_random_tuples(10, 3, [str, float, int])
    sort_insertion(list3, key=lambda x: x[2])

    print("Sorted by item 2 (int):")
    for t in list3:
        print(t)


if __name__ == "__main__":
    main()
