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
        if index > self.capacity:
            print('Error: Index out of range')
        return self.array[index]
    
    def displayArray(self):
        for k in range(self.count):
            print(self.array[k])
    
    def append(self, element):
        if self.count == self.capacity:
            self._resize(2 * self.capacity)

        self.array[self.count] = element
        self.count += 1

    def _resize(self, new_capacity):
        newArray = self.make_array(new_capacity)
        for k in range(self.count):
            newArray[k] = self.array[k]
        
        self.array = newArray
        self.capacity = new_capacity

    def make_array(self, new_capacity):
        return (new_capacity * ctypes.py_object)()
    
ar = DynamicArray()
ar.displayArray()
print(ar.__len__())
ar.append(3)
ar.append(8)
ar.append(398)
ar.append(0)
ar.append(2)
print(ar.__len__())
ar.displayArray()