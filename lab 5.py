class Array:
    def __init__(self, size, datatype):
        self.size = size
        self.datatype = datatype
        self.data = [None] * size
        self.length = 0

    def append(self, element):
        if self.length == self.size:
            self.resize()
        self.data[self.length] = element
        self.length += 1

    def get(self, index):
        if 0 <= index < self.length:
            return self.data[index]
        else:
            return None

    def set(self, index, value):
        if 0 <= index < self.length:
            self.data[index] = value

    def size(self):
        return self.length

    def capacity(self):
        return self.size

    def display(self):
        for i in range(self.length):
            print(self.data[i])

    def resize(self):
        self.size *= 2
        new_data = [None] * self.size
        for i in range(self.length):
            new_data[i] = self.data[i]
        self.data = new_data

def array_statistics(arr):
    sum = 0
    for i in range(arr.size()):
        sum += arr.get(i)
        average = sum / arr.size()
    print("Sum:", sum)
    print("Average:", average)

def reverse_strings(arr):
    reversed_arr = Array(arr.size, str)
    for i in range(arr.size - 1, -1, -1):
        reversed_arr.append(arr.get(i))
    reversed_arr.display()

def max_occurrence(arr):
    count = {}
    max_count = 0
    max_occurrences = []
    for i in range(arr.size):
        element = arr.get(i)
        if element in count:
            count[element] += 1
        else:
            count[element] = 1
        if count[element] > max_count:
            max_count = count[element]
            max_occurrences = [element]
        elif count[element] == max_count:
            max_occurrences.append(element)
    print("Most frequent integer(s):", max_occurrences)

def is_anagram(str1, str2):
    return sorted(str1) == sorted(str2)

def string_anagram_checker(arr):
    anagram_pairs = []
    for i in range(arr.size - 1):
        for j in range(i + 1, arr.size):
            if is_anagram(arr.get(i), arr.get(j)):
                anagram_pairs.append((arr.get(i), arr.get(j)))
    print("Anagram pairs:", anagram_pairs)



arr = Array(5, int)
arr.append(1)
arr.append(2)
arr.append(3)
arr.append(4)
arr.append(5)

print("Array elements:")
arr.display()

input_array = input("Enter:")
input 

strings = Array(3, str)
strings.append("tayyab")
strings.append("babar")
strings.append("dsa")

print("Reversed strings:")
reverse_strings(arr)

integers = Array(6, int)
integers.append(1)
integers.append(2)
integers.append(2)
integers.append(3)
integers.append(3)
integers.append(3)

max_occurrence(integers)

str_arr = Array(4, str)
str_arr.append("listen")
str_arr.append("silent")
str_arr.append("university")
str_arr.append("lahore")

string_anagram_checker(str_arr)