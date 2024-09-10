class Node:
    def __init__(self, type, data, children):
        self.type = type
        self.data = data
        self.children = children

    def add_child(self, node):
        self.children.append(node)

    @property
    def label(self):
        return self.data

    def __getitem__(self, item):
        return self.children[item]

    def __iter__(self):
        return iter(self.children)

    def __len__(self):
        return len(self.children)

    def __repr__(self):
        return f"<Node ({self.type}): {repr(self.data)} [{len(self.children)}...]>"

    def __str__(self):
        return f"[{self.type}: {self.label} {' '.join(str(child) for child in self.children)}]"


class FilebodyNode(Node):
    def __init__(self):
        super().__init__("filebody", "", [])


class BodyNode(Node):
    def __init__(self):
        super().__init__("body", "", [])


class FunctionNode(Node):
    def __init__(self, ident, args, body):
        super().__init__("function", ident, [body])
        self.args = args

    @property
    def label(self):
        return self.data + " " + ",".join(self.args)

    @property
    def arity(self):
        return len(self.args)

    @property
    def body(self):
        return self.children[0]

class VariableNode(Node):
    def __init__(self, ident):
        super().__init__("variable", ident, [])


class IntegerNode(Node):
    def __init__(self, intlit):
        super().__init__("integer", intlit, [])
