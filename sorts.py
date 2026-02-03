def quicksort(a):
    if len(a) < 2:
        return

    stack = [(0, len(a) - 1)]
    while stack:
        l, r = stack.pop()
        while l < r:
            pivot = a[(l + r) // 2]
            i, j = l, r
            while i <= j:
                while a[i] < pivot:
                    i += 1
                while a[j] > pivot:
                    j -= 1

                if i <= j:
                    a[i], a[j] = a[j], a[i]
                    i += 1
                    j -= 1

            if (j - l) < (r - i):
                if i < r:
                    stack.append((i, r))
                r = j
            else:
                if l < j:
                    stack.append((l, j))
                l = i


def heapsort(a):
    n = len(a)
    if n < 2:
        return

    def sift_down(start, end):
        root = start
        while True:
            child = 2 * root + 1
            if child > end:
                break

            if child + 1 <= end and a[child] < a[child + 1]:
                child += 1

            if a[root] < a[child]:
                a[root], a[child] = a[child], a[root]
                root = child
            else:
                break

    for start in range((n - 2) // 2, -1, -1):
        sift_down(start, n - 1)

    for end in range(n - 1, 0, -1):
        a[0], a[end] = a[end], a[0]
        sift_down(0, end - 1)


def mergesort(a):
    n = len(a)
    if n < 2:
        return

    tmp = [None] * n

    def sort(lo, hi):
        if hi - lo <= 1:
            return

        mid = (lo + hi) // 2

        sort(lo, mid)
        sort(mid, hi)

        i, j, k = lo, mid, lo
        while i < mid and j < hi:
            if a[i] <= a[j]:
                tmp[k] = a[i]; i += 1
            else:
                tmp[k] = a[j]; j += 1
            k += 1

        while i < mid:
            tmp[k] = a[i]; i += 1; k += 1
        while j < hi:
            tmp[k] = a[j]; j += 1; k += 1

        a[lo:hi] = tmp[lo:hi]

    sort(0, n)