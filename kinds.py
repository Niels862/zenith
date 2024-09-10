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


class NumberObject(Object):
    def __init__(self, num):
        super().__init__()
        self.num = num

    def __str__(self) -> str:
        return str(self.num)

    def __int__(self):
        return self.num

    def __add__(self, other):
        return NumberObject(self.num + other.num)

    def __sub__(self, other):
        return NumberObject(self.num + other.num)
    
    def __mul__(self, other):
        return NumberObject(self.num * other.num)
    
    def __truediv__(self, other):
        return NumberObject(self.num / other.num)
    
    def __mod__(self, other):
        return NumberObject(self.num % other.num)


class StringObject(Object):
    def __init__(self, data):
        super().__init__()
        self.data = data
    
    def __str__(self) -> str:
        return self.data

    def __add__(self, other):
        return StringObject(self.data + other.data)


class ListObject(Object):
    def __init__(self):
        super().__init__()
        self.data = {}

    def __str__(self) -> str:
        return str(self.data)
