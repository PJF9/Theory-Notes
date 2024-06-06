from random import shuffle


def merge_sort(l):
    
    def merge(l, first, mid, last):
        b = []
        
        i, j, k = first, mid + 1, 0

        while (i <= mid) and (j <= last):
            if (l[i] < l[j]):
                b.append(l[i])
                k += 1
                i += 1
            else:
                b.append(l[j])
                k += 1
                j += 1
        
        while (i <= mid):
            b.append(l[i])
            k += 1
            i += 1

        while (j <= last):
            b.append(l[j])
            k += 1
            j += 1

        for i in range(k):
            l[first + i] = b[i]

    def recursive(l, first, last):
        if (first >= last):
            return
        
        mid = (first + last) // 2

        recursive(l, first, mid)
        recursive(l, mid+1, last)
        merge(l, first, mid, last)

    
    recursive(l, 0, len(l)-1)


l = list(range(100))
shuffle(l)

merge_sort(l)

print(l)
