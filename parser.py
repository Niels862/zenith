from tree import *
from text import Text
from kinds import *


class Parser:
    def __init__(self, text):
        self.text: Text = text

    def parse(self):
        return self.parse_filebody()
    
    def parse_filebody(self):
        node = FilebodyNode()
        while not self.text.end():
            node.add_child(self.parse_function())
        return node

    def parse_function(self):
        ident = self.text.get()
        args = []
        while self.text.peek().isalpha():
            args.append(self.text.get())
        if self.text.peek() == ",":
            self.text.next()
        body = self.parse_body()
        return FunctionNode(ident, args, body)
        
    def parse_body(self):
        body = BodyNode()
        while not self.text.peek() == ".":
            if self.text.end():
                raise SyntaxError()
            body.add_child(self.parse_expression())
        self.text.next()
        return body

    def parse_expression(self):
        c = self.text.get()
        if c.isdigit():
            return IntegerNode(NumberObject(int(c)))
        else:
            return VariableNode(c)
        raise SyntaxError()
