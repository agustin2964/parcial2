class Cola:

    def __init__(self):
        self.__elements = []

    def arrive(self, value):
        self.__elements.append(value)

    def atencion(self):
        return (
            self.__elements.pop(0)
            if self.__elements
            else None
        )

    def size(self):
        return len(self.__elements)
    
    def on_front(self):
        return (
            self.__elements[0]
            if self.__elements
            else None
        )

    def move_to_end(self):
        if self.__elements:
            value = self.atencion()
            self.arrive(value)
            return value
    
    def show(self):
        for i in range(len(self.__elements)):
            print(self.move_to_end())
