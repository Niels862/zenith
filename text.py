class Text:
    def __init__(self, data):
        self.data = data
        self.p = 0
        self.skip()
    
    def end(self) -> bool:
        return self.p >= len(self.data)

    def skip(self):
        if self.end():
            return
        
        c = self.data[self.p]
        while not self.end() and c in " \t\n\r":
            self.p += 1

    def next(self):
        if self.p < len(self.data):
            self.p += 1
            self.skip()

        return self.peek()

    def peek(self) -> str:
        if self.end():
            return ""
        
        return self.data[self.p]

    def get(self) -> str:
        c = self.peek()
        self.next()
        
        return c
