from random import shuffle


def quick_sort(l):
    
    def partition(l, first, last):
        x = l[(first + last) // 2]
        i, j = first, last

        while True:
            while (l[i] < x):
                i += 1
            while (l[j] > x):
                j -= 1

            if (i >= j):
                break

            l[i], l[j] = l[j], l[i]

            i += 1
            j -= 1
        
        return j

    def recursive(l, first, last):
        if (first >= last):
            return
        
        i = partition(l, first, last)

        recursive(l, first, i)
        recursive(l, i+1, last)

    recursive(l, 0, len(l) - 1)


l = list(range(100))
shuffle(l)

quick_sort(l)

print(l)
