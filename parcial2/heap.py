from itertools import count

class HeapMax:

    def __init__(self):
        self.elements = []
        self.c=count(start=0, step=-1)
    
    def size(self):
        return len(self.elements)

    def add(self, value):
        self.elements.append(value)
        self.float(self.size()-1)
    
    def remove(self):
        last = self.size() -1
        self.interchange(0, last)
        value = self.elements.pop()
        self.sink(0)
        return value

    def float(self, index):
        father = (index - 1) // 2
        while index > 0 and self.elements[index] > self.elements[father]:
            # print(f'flotar desde {index} a {father}')
            self.interchange(index, father)
            index = father
            father = (index - 1) // 2

    def sink(self, index):
        left_son = (2 * index) + 1
        control = True
        while control and left_son < self.size():
            right_son = left_son + 1

            mayor = left_son
            if right_son < self.size():
                if self.elements[right_son] > self.elements[mayor]:
                    mayor = right_son

            if self.elements[index] < self.elements[mayor]:
                # print(f'hundir desde {index} a {mayor}')
                self.interchange(index, mayor)
                index = mayor
                left_son = (2 * index) + 1
            else:
                control = False


    def interchange(self, index_1, index_2):
        self.elements[index_1], self.elements[index_2] = self.elements[index_2], self.elements[index_1]

    def heapsort(self):
        result = []
        while self.size() > 0:
            result.append(self.remove())
        return result

    def arrive(self, value, priority):
        # priority 1-low, 2-medium, 3-high
        self.add((priority, next(self.c), value))
    
    def attention(self):
        value = self.remove()
        return value[-1]


class HeapMin:

    def __init__(self):
        self.elements = []
    
    def size(self):
        return len(self.elements)

    def add(self, value):
        self.elements.append(value)
        self.float(self.size()-1)
    
    def search(self, value):
        for index, element in enumerate(self.elements):
            if element[1][0] == value:
                return index

    def remove(self):
        last = self.size() -1
        self.interchange(0, last)
        value = self.elements.pop()
        self.sink(0)
        return value

    def float(self, index):
        father = (index - 1) // 2
        while index > 0 and self.elements[index] < self.elements[father]:
            self.interchange(index, father)
            index = father
            father = (index - 1) // 2

    def sink(self, index):
        left_son = (2 * index) + 1
        control = True
        while control and left_son < self.size():
            right_son = left_son + 1

            minor = left_son
            if right_son < self.size():
                if self.elements[right_son] < self.elements[minor]:
                    minor = right_son

            if self.elements[index] > self.elements[minor]:
                self.interchange(index, minor)
                index = minor
                left_son = (2 * index) + 1
            else:
                control = False


    def interchange(self, index_1, index_2):
        self.elements[index_1], self.elements[index_2] = self.elements[index_2], self.elements[index_1]

    # def monticulizar

    def heapsort(self):
        result = []
        while self.size() > 0:
            result.append(self.remove())
        return result

    def arrive(self, value, priority):
        # priority 1-low, 2-medium, 3-high
        self.add([priority, value])
    
    def attention(self):
        value = self.remove()
        return value

    def change_priority(self, index, new_priority):
        if index < len(self.elements):
            previous_priority = self.elements[index][0]
            self.elements[index][0] = new_priority
            if new_priority > previous_priority:
                self.sink(index)
            elif new_priority < previous_priority:
                self.float(index)