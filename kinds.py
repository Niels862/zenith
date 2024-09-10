class Object:
    def __init__(self):
        pass

    def __str__(self) -> str:
        return NotImplemented


class FunctionObject(Object):
    def __init__(self, node):
        super().__init__()
        self.node = node
        self.arity = node.arity


class BuiltinFunctionObject(Object):
    def __init__(self, func, arity):
        super().__init__()
        self.func = func
        self.arity = arity

    def call(self, args):
        assert len(args) == self.arity
        return self.func(*args)

    def __str__(self) -> str:
        return str(self.func)


class NumberObject(Object):
    def __init__(self, num):
        super().__init__()
        self.num = int(num)

    def __str__(self) -> str:
        return str(self.num)

    def __int__(self):
        return self.num

    def __add__(self, other):
        return NumberObject(self.num + other.num)

    def __sub__(self, other):
        return NumberObject(self.num + other.num)
    
    def __mul__(self, other):
        return NumberObject(int(self) * int(other))
 
    def __truediv__(self, other):
        return NumberObject(self.num / other.num)
    
    def __mod__(self, other):
        return NumberObject(self.num % other.num)

    def __pow__(self, exp):
        return NumberObject(self.num ** exp.num)

    def __eq__(self, other):
        return NumberObject(self.num == other.num)
    
    def __lt__(self, other):
        return NumberObject(self.num < other.num)
    
    def __gt__(self, other):
        return NumberObject(self.num > other.num)


class StringObject(Object):
    def __init__(self, data):
        super().__init__()
        self.data = data
    
    def __int__(self):
        if len(self.data) > 0:
            return int(self.data[0])
        return 0

    def __str__(self) -> str:
        return self.data

    def length(self):
        return NumberObject(len(self.data))

    def __getitem__(self, item):
        return StringObject(self.data[int(item)])

    def __add__(self, other):
        return StringObject(self.data + other.data)


class ListObject(Object):
    def __init__(self):
        super().__init__()
        self.data = {}

    def length(self):
        return NumberObject(max(self.data.keys()))

    def __getitem__(self, item):
        return self.data[item]

    def __str__(self) -> str:
        return str(self.data)
