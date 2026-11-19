"""
Original implementation by ehis's Gist sort.py (forked from mattmcclean/sort.py)
https://gist.github.com/ehis/3979310
Accessed 2026-11-19; adapted for Flask portfolio integration.
"""

def _record(steps, arr, active=(), swapped=(), sorted_indices=()):
    steps.append({
        "values": list(arr),
        "active": list(active),
        "swapped": list(swapped),
        "sorted": list(sorted_indices),
    })


# bubble sort
def bubble_sort(list2):
    arr = list(list2)
    for i in range(0, len(arr) - 1):
        swap_test = False
        for j in range(0, len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swap_test = True
        if swap_test is False:
            break
    return arr


def _bubble_sort_steps(items):
    arr = list(items)
    steps = []
    n = len(arr)
    done = set()
    _record(steps, arr, sorted_indices=done)
    for i in range(0, n - 1):
        swap_test = False
        for j in range(0, n - i - 1):
            _record(steps, arr, active=(j, j + 1), sorted_indices=done)
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swap_test = True
                _record(steps, arr, swapped=(j, j + 1), sorted_indices=done)
        done.add(n - 1 - i)
        if not swap_test:
            done.update(range(0, n))
            _record(steps, arr, sorted_indices=done)
            break
        _record(steps, arr, sorted_indices=done)
    done.update(range(0, n))
    _record(steps, arr, sorted_indices=done)
    return arr, steps


# selection sort
def selection_sort(list2):
    arr = list(list2)
    for i in range(0, len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr


def _selection_sort_steps(items):
    arr = list(items)
    steps = []
    n = len(arr)
    done = set()
    _record(steps, arr, sorted_indices=done)
    for i in range(0, n):
        min_idx = i
        for j in range(i + 1, n):
            _record(steps, arr, active=(min_idx, j), sorted_indices=done)
            if arr[j] < arr[min_idx]:
                min_idx = j
                _record(steps, arr, active=(i, min_idx), sorted_indices=done)
        if i != min_idx:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
            _record(steps, arr, swapped=(i, min_idx), sorted_indices=done)
        done.add(i)
        _record(steps, arr, sorted_indices=done)
    return arr, steps


# insertion sort
def insertion_sort(list2):
    arr = list(list2)
    for i in range(1, len(arr)):
        save = arr[i]
        j = i
        while j > 0 and arr[j - 1] > save:
            arr[j] = arr[j - 1]
            j -= 1
        arr[j] = save
    return arr


def _insertion_sort_steps(items):
    arr = list(items)
    steps = []
    _record(steps, arr)
    for i in range(1, len(arr)):
        save = arr[i]
        j = i
        _record(steps, arr, active=(j,))
        while j > 0 and arr[j - 1] > save:
            _record(steps, arr, active=(j - 1, j))
            arr[j] = arr[j - 1]
            j -= 1
            _record(steps, arr, swapped=(j, j + 1))
        arr[j] = save
        _record(steps, arr, swapped=(j,))
    _record(steps, arr, sorted_indices=range(0, len(arr)))
    return arr, steps


# quick sort
def quick_sort(list2):
    arr = list(list2)
    if len(arr) > 1:
        _quick_sort_r(arr, 0, len(arr) - 1)
    return arr


def _quick_sort_r(list2, first, last):
    if last > first:
        pivot = _partition(list2, first, last)
        _quick_sort_r(list2, first, pivot - 1)
        _quick_sort_r(list2, pivot + 1, last)


def _partition(list2, first, last):
    sred = (first + last) // 2
    if list2[first] > list2[sred]:
        list2[first], list2[sred] = list2[sred], list2[first]
    if list2[first] > list2[last]:
        list2[first], list2[last] = list2[last], list2[first]
    if list2[sred] > list2[last]:
        list2[sred], list2[last] = list2[last], list2[sred]
    list2[sred], list2[first] = list2[first], list2[sred]
    pivot = first
    i = first + 1
    j = last

    while True:
        while i <= last and list2[i] <= list2[pivot]:
            i += 1
        while j >= first and list2[j] > list2[pivot]:
            j -= 1
        if i >= j:
            break
        else:
            list2[i], list2[j] = list2[j], list2[i]
    list2[j], list2[pivot] = list2[pivot], list2[j]
    return j


def _quick_sort_steps(items):
    arr = list(items)
    steps = []
    _record(steps, arr)

    def partition_s(first, last):
        sred = (first + last) // 2
        if arr[first] > arr[sred]:
            arr[first], arr[sred] = arr[sred], arr[first]
            _record(steps, arr, swapped=(first, sred))
        if arr[first] > arr[last]:
            arr[first], arr[last] = arr[last], arr[first]
            _record(steps, arr, swapped=(first, last))
        if arr[sred] > arr[last]:
            arr[sred], arr[last] = arr[last], arr[sred]
            _record(steps, arr, swapped=(sred, last))
        arr[sred], arr[first] = arr[first], arr[sred]
        _record(steps, arr, swapped=(sred, first))

        pivot = first
        i = first + 1
        j = last
        while True:
            while i <= last and arr[i] <= arr[pivot]:
                _record(steps, arr, active=(pivot, i))
                i += 1
            while j >= first and arr[j] > arr[pivot]:
                _record(steps, arr, active=(pivot, j))
                j -= 1
            if i >= j:
                break
            arr[i], arr[j] = arr[j], arr[i]
            _record(steps, arr, swapped=(i, j))
        arr[j], arr[pivot] = arr[pivot], arr[j]
        _record(steps, arr, swapped=(j, pivot))
        return j

    def rec(first, last):
        if last > first:
            p = partition_s(first, last)
            rec(first, p - 1)
            rec(p + 1, last)

    if len(arr) > 1:
        rec(0, len(arr) - 1)
    _record(steps, arr, sorted_indices=range(0, len(arr)))
    return arr, steps


# heap sort
def heap_sort(list2):
    arr = list(list2)
    if len(arr) > 1:
        first = 0
        last = len(arr) - 1
        _create_heap(arr, first, last)
        for i in range(last, first, -1):
            arr[i], arr[first] = arr[first], arr[i]
            _establish_heap_property(arr, first, i - 1)
    return arr


def _create_heap(list2, first, last):
    i = last // 2
    while i >= first:
        _establish_heap_property(list2, i, last)
        i -= 1


def _establish_heap_property(list2, first, last):
    while 2 * first + 1 <= last:
        k = 2 * first + 1
        if k < last and list2[k] < list2[k + 1]:
            k += 1
        if list2[first] >= list2[k]:
            break
        list2[first], list2[k] = list2[k], list2[first]
        first = k


def _heap_sort_steps(items):
    arr = list(items)
    steps = []
    done = set()
    _record(steps, arr)

    def sift(first, last):
        curr = first
        while 2 * curr + 1 <= last:
            k = 2 * curr + 1
            if k < last and arr[k] < arr[k + 1]:
                k += 1
            _record(steps, arr, active=(curr, k), sorted_indices=done)
            if arr[curr] >= arr[k]:
                break
            arr[curr], arr[k] = arr[k], arr[curr]
            _record(steps, arr, swapped=(curr, k), sorted_indices=done)
            curr = k

    if len(arr) > 1:
        last = len(arr) - 1
        i = last // 2
        while i >= 0:
            sift(i, last)
            i -= 1
        for i in range(last, 0, -1):
            arr[i], arr[0] = arr[0], arr[i]
            _record(steps, arr, swapped=(0, i), sorted_indices=done)
            done.add(i)
            sift(0, i - 1)
    done.update(range(0, len(arr)))
    _record(steps, arr, sorted_indices=done)
    return arr, steps


# merge sort
def merge_sort(list2):
    arr = list(list2)
    if len(arr) > 1:
        _merge_sort_r(arr, 0, len(arr) - 1)
    return arr


def _merge_sort_r(list2, first, last):
    if first < last:
        sred = (first + last) // 2
        _merge_sort_r(list2, first, sred)
        _merge_sort_r(list2, sred + 1, last)
        _merge(list2, first, last, sred)


def _merge(list2, first, last, sred):
    helper_list = []
    i = first
    j = sred + 1
    while i <= sred and j <= last:
        if list2[i] <= list2[j]:
            helper_list.append(list2[i])
            i += 1
        else:
            helper_list.append(list2[j])
            j += 1
    while i <= sred:
        helper_list.append(list2[i])
        i += 1
    while j <= last:
        helper_list.append(list2[j])
        j += 1
    for k in range(0, last - first + 1):
        list2[first + k] = helper_list[k]


def _merge_sort_steps(items):
    arr = list(items)
    steps = []
    _record(steps, arr)

    def merge_s(first, last, sred):
        helper_list = []
        i = first
        j = sred + 1
        while i <= sred and j <= last:
            _record(steps, arr, active=(i, j))
            if arr[i] <= arr[j]:
                helper_list.append(arr[i])
                i += 1
            else:
                helper_list.append(arr[j])
                j += 1
        while i <= sred:
            helper_list.append(arr[i])
            i += 1
        while j <= last:
            helper_list.append(arr[j])
            j += 1
        for k in range(0, last - first + 1):
            arr[first + k] = helper_list[k]
            _record(steps, arr, swapped=(first + k,))

    def rec(first, last):
        if first < last:
            sred = (first + last) // 2
            rec(first, sred)
            rec(sred + 1, last)
            merge_s(first, last, sred)

    if len(arr) > 1:
        rec(0, len(arr) - 1)
    _record(steps, arr, sorted_indices=range(0, len(arr)))
    return arr, steps


ALGORITHMS = {
    "bubble": ("Bubble Sort", bubble_sort),
    "selection": ("Selection Sort", selection_sort),
    "insertion": ("Insertion Sort", insertion_sort),
    "quick": ("Quick Sort", quick_sort),
    "heap": ("Heap Sort", heap_sort),
    "merge": ("Merge Sort", merge_sort),
}

STEP_ALGORITHMS = {
    "bubble": _bubble_sort_steps,
    "selection": _selection_sort_steps,
    "insertion": _insertion_sort_steps,
    "quick": _quick_sort_steps,
    "heap": _heap_sort_steps,
    "merge": _merge_sort_steps,
}


def run_sort(algorithm_key, items):
    label, fn = ALGORITHMS.get(algorithm_key, ALGORITHMS["bubble"])
    return label, fn(items)


def run_sort_with_steps(algorithm_key, items):
    label, fn = ALGORITHMS.get(algorithm_key, ALGORITHMS["bubble"])
    step_fn = STEP_ALGORITHMS.get(algorithm_key, _bubble_sort_steps)
    sorted_list, steps = step_fn(items)
    return label, sorted_list, steps