class InversionCalculator(object):
    def __init__(self):
        self.input_array = []
        self.input_inversions = 0

    @property
    def inversions(self):
        return self.input_inversions

    @property
    def array(self):
        return self.input_array

    def read_input(self, input_file=None):
        if input_file is None:
            self.input_array = [int(elem) for elem in input().split()]
            return
        with open(input_file) as numbers:
            for number in numbers:
                self.input_array.append(int(number))

    def merge_sort(self, array=None):
        if array is None:
            array = self.input_array
        return self._sort(array)

    def _sort(self, array):
        if len(array) <= 1:
            return array
        mid = (len(array)) // 2
        first_half = self._sort(array[:mid])
        second_half = self._sort(array[mid:])
        return self._merge(array, first_half, second_half)

    def _merge(self, array, first_half, second_half):
        i, j, k = 0, 0, 0
        while j < len(first_half) and k < len(second_half):
            if first_half[j] <= second_half[k]:
                array[i] = first_half[j]
                j += 1
            else:
                array[i] = second_half[k]
                k += 1
                self.input_inversions += (len(first_half) - j)
            i += 1
        while j < len(first_half):
            array[i] = first_half[j]
            j += 1
            i += 1
        while k < len(second_half):
            array[i] = second_half[k]
            k += 1
            i += 1
        return array

if __name__ == '__main__':
    calculator = InversionCalculator()
    calculator.read_input("ints.txt")
    calculator.merge_sort()
    print(calculator.inversions)

#Output:2407905288
