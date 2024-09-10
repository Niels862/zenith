from parser import Parser
from text import Text
from interpreter import Interpreter


def main():
    with open("main.zn", "r") as file:
        ast = Parser(Text(file.read())).parse()
    print(ast)
    ret = Interpreter(ast).interpret()
    print(ret)


if __name__ == "__main__":
    main()
