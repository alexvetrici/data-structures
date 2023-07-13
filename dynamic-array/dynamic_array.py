# Logic for dynamic array implementation
import ctypes

class DynamicArray():
    def __init__(self):
        self.count = 0
        self.capacity = 1
        self.array = self.make_array(self.capacity)

    def __len__(self):
        return self.count
    
    def __getitem__(self, index):
        if not 0 <= index < self.count:
            print("Error: Index out of bound")
            return
        return self.array[index]
    
    def displayArray(self):
        for k in range(self.count):
            print(self.array[k])
    
    def append(self, element):
        if self.count == self.capacity:
            self._resize(2 * self.capacity)

        self.array[self.count] = element
        self.count += 1

    def insertAt(self, element, index):
        if index > self.count:
            print("Enter appropriate index..")
            return

        if self.count == self.capacity:
            self._resize(2 * self.capacity)

        temp = self.count
        while temp != index:
            self.array[temp] = self.array[temp - 1]
            temp -= 1

        self.array[index] = element
        self.count += 1

    def removeAt(self, index):
        if self.count == 0:
            print("Array is empty, removing is not possible")
            return
        
        if index >= self.count:
            print("Error: Index out of bound, removig is not possible")
            return

        if index == self.count - 1:
            self.array[self.count] = 0
            self.count -= 1
            return
        
        for k in range(index, self.count - 1):
            self.array[k] = self.array[k + 1]

        self.array[self.count - 1] = 0
        self.count -= 1

    def _resize(self, new_capacity):
        newArray = self.make_array(new_capacity)
        for k in range(self.count):
            newArray[k] = self.array[k]
        
        self.array = newArray
        self.capacity = new_capacity

    def make_array(self, new_capacity):
        return (new_capacity * ctypes.py_object)()