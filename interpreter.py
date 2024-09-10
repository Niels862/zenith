from tree import *
from kinds import *
from operator import add, sub, mul, truediv, mod, pow, eq, lt, gt


class Frame:
    def __init__(self):
        self.map = {}


class Interpreter:
    def __init__(self, ast):
        self.ast: Node = ast
        self.decls = {}
        self.get_decls()
        self.frames = []
        self.entry = self.get_entry()

    def get_decls(self):
        ops = {
            "+": (add, 2),
            "-": (sub, 2),
            "*": (mul, 2),
            "/": (truediv, 2),
            "%": (mod, 2),
            "^": (pow, 2),
            "=": (eq, 2),
            "<": (lt, 2),
            ">": (gt, 2),
            "⤶": (lambda: StringObject(input()), 0),
            "⤷": (lambda x: [print(x), x][1], 1),
            "∅": (lambda: ListObject(), 0)
        }
        for key, (func, arity) in ops.items():
            self.decls[key] = BuiltinFunctionObject(func, arity)
        for node in self.ast:
            if isinstance(node, FunctionNode):
                self.decls[node.data] = FunctionObject(node)
            else:
                raise RuntimeError()

    def get_entry(self):
        entry = self.lookup("m")
        assert isinstance(entry, FunctionObject)
        return entry

    def top_frame(self):
        if len(self.frames) > 0:
            return self.frames[-1]
        return Frame()

    def set_var(self, ident, value):
        if len(self.frames) > 0:
            self.frames[-1].map[ident] = value
        else:
            raise RuntimeError()

    def lookup(self, ident):
        frame = self.top_frame()
        if ident in frame.map:
            return frame.map[ident]
        if ident in self.decls:
            return self.decls[ident]
        raise LookupError(ident)

    def interpret(self):
        return self.call_func(self.entry, [])

    def call_func(self, sym, args):
        if isinstance(sym, FunctionObject):
            node = sym.node
            frame = Frame()
            for key, value in zip(node.args, args, strict=True):
                frame.map[key] = value
            self.frames.append(frame)
            ret = self.eval_expr(node.body)
            self.frames.pop()
            return ret
        if isinstance(sym, BuiltinFunctionObject):
            return sym.call(args)
        raise RuntimeError()

    def eval_expr(self, node):
        last = None
        i = 0
        while i < len(node):
            i, last = self.eval_expr_part(node, i)
        return last

    def eval_expr_part(self, node, i):
        expr = node[i]
        if isinstance(expr, IntegerNode):
            return (i + 1, expr.data)
        elif isinstance(expr, VariableNode):
            if expr.data == "⟳":
                j, n = self.eval_expr_part(node, i + 1)
                return self.eval_loop(node, j, n)
            if expr.data == "←":
                j, (map, key) = self.eval_assignable(node, i + 1)
                j, value = self.eval_expr_part(node, j)
                map[key] = value
                return j, value
            sym = self.lookup(expr.data)
            if isinstance(sym, FunctionObject) \
                    or isinstance(sym, BuiltinFunctionObject):
                j, args = self.eval_gather_args(node, i + 1, sym.arity)
                return (j, self.call_func(sym, args))
            return (i + 1, sym)
        else:
            raise RuntimeError()

    def skip_expr_part(self, node, i):
        expr = node[i]
        if isinstance(expr, IntegerNode):
            return i + 1
        if isinstance(expr, VariableNode):
            if expr.data == "⟳" or expr.data == "←":
                arity = 2
            else:
                sym = self.lookup(expr.data)
                if isinstance(sym, FunctionObject) \
                        or isinstance(sym, BuiltinFunctionObject):
                    arity = sym.arity
                else:
                    return i + 1
            j = i + 1
            for k in range(arity):
                j = self.skip_expr_part(node, j)
            return j
        raise RuntimeError()

    def eval_assignable(self, node, i):
        expr = node[i]
        if isinstance(expr, VariableNode):
            return (i + 1, (self.top_frame().map, expr.data))
        raise RuntimeError()

    def eval_gather_args(self, node, i, n):
        args = []
        for k in range(n):
            i, param = self.eval_expr_part(node, i)
            args.append(param)
        return (i, args)

    def eval_loop(self, node, i, n):
        s = 0
        j = 0
        if not int(n):
            return self.skip_expr_part(node, i), NumberObject(0)
        for it in range(int(n)):
            self.set_var("i", NumberObject(it))
            j, res = self.eval_expr_part(node, i)
            s += int(res)
        return j, NumberObject(s)
