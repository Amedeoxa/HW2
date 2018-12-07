import random
from timeit import Timer
import matplotlib.pyplot as plt


def partition(arr, low, high):
    divider = (low - 1)
    pivot = arr[high]
    for j in range(low, high):
        if arr[j] <= pivot:
            divider = divider + 1
            arr[divider], arr[j] = arr[j], arr[divider]

    arr[divider + 1], arr[high] = arr[high], arr[divider + 1]
    return divider + 1


def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)

    return arr


def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        lefthalf = arr[:mid]
        righthalf = arr[mid:]

        merge_sort(lefthalf)
        merge_sort(righthalf)

        i = 0
        j = 0
        k = 0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                arr[k] = lefthalf[i]
                i = i+1
            else:
                arr[k] = righthalf[j]
                j = j+1
            k = k+1

        while i < len(lefthalf):
            arr[k] = lefthalf[i]
            i = i+1
            k = k+1

        while j < len(righthalf):
            arr[k] = righthalf[j]
            j = j+1
            k = k+1
    return arr


def sort_time(num):  # max length of lists we want to sort (10^num). would not go over 6
    quick = []  #
    merge = []  # where we will store the data for the plot
    x = []
    for i in range(1, num+1):  # we loop to run the test on lists from 10 to 10^num
        x.append(i-1)
        avg_q = 0
        avg_m = 0
        n = 5                       # we loop again to time our algorithms on lists of a given length n times
        for j in range(1, n+1):     # and get an average of the time it takes for a given length
            lst = list(range(10**i))  #
            random.shuffle(lst)       # generator for list of 10^i numbers that is shuffled
            global a                  #
            global b                  # two copies of the list, so we can time both algorithms on the same data
            a = lst.copy()            #
            b = lst.copy()            #
            s = 'quick_sort(a, 0, len(a)-1)'
            t1 = Timer(s, globals=globals())  # timer for quick_sort
            time1 = t1.timeit(1)
            avg_q += time1
            s = 'merge_sort(b)'
            t2 = Timer(s, globals=globals())  # timer for merge_sort
            time2 = t2.timeit(1)
            avg_m += time2
        quick.append(avg_q/n)
        merge.append(avg_m/n)
        print('quick_sort = %04.6f  merge_sort = %2.6f  q/m = %5.6f length list = %1d' % (avg_q/n, avg_m/n, avg_m/avg_m, 10**i))

# plotting the data
    plt.subplot(211)
    plt.title('Sorting Speed')
    plt.xticks(x, ['10', r'$10^2$', r'$10^3$', r'$10^4$', r'$10^5$', r'$10^6$'])
    plt.xlabel('length list')
    plt.yticks(rotation=45)
    plt.ylabel('seconds',)
    plt.plot(quick, '^-', label='quick sort', linewidth=1.5, markersize=2)
    plt.plot(merge, 'o-', label='merge sort', linewidth=1.5, markersize=2)
    plt.gca().yaxis.grid(True)
    plt.legend()

    plt.subplot(212)
    plt.title('logarithmic scale')
    plt.xticks(x, ['10', r'$10^2$', r'$10^3$', r'$10^4$', r'$10^5$', r'$10^6$'])
    plt.xlabel('length list')
    plt.yticks(rotation=45)
    plt.ylabel('seconds')
    plt.yscale('log')
    plt.plot(quick, '^-', label='quick sort', linewidth=1.2, markersize=2.8)
    plt.plot(merge, 'o-', label='merge sort', linewidth=1.2, markersize=2.5)
    plt.gca().yaxis.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.savefig('time_plot')
    plt.show()


if __name__ == '__main__':
    sort_time(6)
