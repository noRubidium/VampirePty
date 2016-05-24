def merge_sort(array, holder, start = 0, end = None, key = lambda x:x ):
    if end == None:
        end = len(array)
    if end - start == 1:
        array[start] = holder[start]
    else:

        mid = ( end + start ) / 2
        merge_sort(holder, array, start, mid, key )
        merge_sort(holder, array, mid, end, key )

        # merge
        i = start
        j = mid
        curr = start
        while i < mid and j < end:
            if key(holder[i]) <= key(holder[j]):
                array[curr] = holder[i]
                i += 1
            else:
                array[curr] = holder[j]
                j += 1
            curr += 1

        while i < mid:
            array[curr] = holder[i]
            i += 1
            curr += 1

        while j < end:
            array[curr] = holder[j]
            j += 1
            curr += 1

# my filter
def my_filter(array, key):
    i = 0
    l = len(array)
    curr = 0
    while i < l:
        if key(array[i]):
            curr += 1
        i += 1
    result = [0] * curr

    i = 0
    curr = 0
    while i < l:
        if key(array[i]):
            result[curr] = array[i]
            curr += 1
        i += 1
        print i
    return result

def main():
    import random
    a = (range(100))
    random.shuffle(a)
    b = a[:]
    merge_sort(a,b)
    print a, b

if __name__ == '__main__':
    main()
