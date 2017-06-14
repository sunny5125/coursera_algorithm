class QuickSorter(object):
    def __init__(self, input_file=None):
        self.input_comparisons = 0
        self.input_array = []
        self.input_invesrions = 0
        self.read_input(input_file)

    @property
    def comparisons(self):
        return self.input_comparisons

    @property
    def array(self):
        return self.input_array

    @array.setter
    def array(self, arr):
        self.input_array = arr

    def read_input(self, input_file=None):
        if input_file is None:
            self.input_array = [int(elem) for elem in input().split()]
            return
        with open(input_file) as numbers:
            for number in numbers:
                self.input_array.append(int(number))

    def sort(self):
        if len(self.input_array) <= 1:
            return
        self._qsort(0, len(self.input_array) - 1)

    def _qsort(self, start, end):
        if start >= end:
            return
        pivot = self.partition(start, end)
        self._qsort(start, pivot - 1)
        self._qsort(pivot + 1, end)

    def partition(self, start, end):
        self.input_comparisons += end - start
        pivot = start
        for i in range(start + 1, end + 1):
            if self.input_array[i] < self.input_array[start]:
                pivot += 1
                self.input_array[i], self.input_array[pivot] = self.input_array[pivot], self.input_array[i]
        self.input_array[start], self.input_array[pivot] = self.input_array[pivot], self.input_array[start]
        return pivot


class QuickSorterFirstElementPivot(QuickSorter):
    def partition(self, start, end):
        return super(QuickSorterFirstElementPivot, self).partition(start, end)


class QuickSorterLastElementPivot(QuickSorter):
    def partition(self, start, end):
        self.input_array[start], self.input_array[end] = self.input_array[end], self.input_array[start]
        return super(QuickSorterLastElementPivot, self).partition(start, end)


class QuickSorterMedianElementPivot(QuickSorter):
    def partition(self, start, end):
        self._choose_median_pivot(start, end)
        return super(QuickSorterMedianElementPivot, self).partition(start, end)

    def _choose_median_pivot(self, start, end):
        length = end - start + 1
        median_index = length // 2 - 1 if length % 2 == 0 else length // 2
        median = start + median_index
        if self.input_array[start] <= self.input_array[median] <= self.input_array[end] or self.input_array[end] <= self.input_array[median] <= \
                self.input_array[start]:
            self.input_array[start], self.input_array[median] = self.input_array[median], self.input_array[start]
        elif self.input_array[median] <= self.input_array[end] <= self.input_array[start] or self.input_array[start] <= self.input_array[end] <= \
                self.input_array[median]:
            self.input_array[start], self.input_array[end] = self.input_array[end], self.input_array[start]

if __name__ == '__main__':
    sorters = (QuickSorterFirstElementPivot('assignment_2.txt'),
               QuickSorterLastElementPivot('assignment_2.txt'),
               QuickSorterMedianElementPivot('assignment_2.txt'))
    for sorter in sorters:
        sorter.sort()
    print(sorters[0].comparisons, sorters[1].comparisons, sorters[2].comparisons)

#Output:162085 164123 138382
