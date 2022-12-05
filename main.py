from inspect import signature, getfullargspec
from typing import Callable


class TableOfTruth:
    def __init__(self, explain: Callable):
        self.var = explain
        self.vector = []

        def vector():
            sig = signature(self.var)
            countOfArguments = len(sig.parameters)
            args = getfullargspec(self.var).args
            arguments = []
            number = 2

            for i in range(len(args)):
                exec(f"{args[i]} = 0")
                arguments.append(0)
            for i in range(2 ** countOfArguments):

                functionArgs = []
                for k in range(countOfArguments):
                    functionArgs.append(arguments[k])
                self.vector.append(bool(self.var(*functionArgs)))

                for j in range(countOfArguments):
                    arguments[j] = (number // (2 ** (countOfArguments - j))) % 2
                    exec(f"{args[j]} = {arguments[j]}")

                number += 2

        vector()

    def __str__(self):
        s = ""
        for i in self.vector:
            s += str(int(self.vector[i]))
        return s

    def __repr__(self):
        s = ""
        for i in self.vector:
            s += str(int(self.vector[i]))
        return s

    def draw(self):

        sig = signature(self.var)
        countOfArguments = len(sig.parameters)
        args = getfullargspec(self.var).args
        arguments = []
        number = 2

        def drawBorder():
            print("#", end="")
            for _ in range(countOfArguments + 1):
                print(" # #", end="")
            print()

        drawBorder()
        for arg in range(countOfArguments):
            print(f"# {args[arg]} ", end="")
        print("# F #")
        drawBorder()
        for i in range(len(args)):
            exec(f"{args[i]} = 0")
            arguments.append(0)
        for i in range(2 ** countOfArguments):
            for j in range(countOfArguments):
                print(f"# {arguments[j]} ", end="")

            print(f"# {int(self.vector[i])} #")

            for j in range(countOfArguments):
                arguments[j] = (number // (2 ** (countOfArguments - j))) % 2
                exec(f"{args[j]} = {arguments[j]}")

            number += 2

        drawBorder()


def f(A, B, C):
    return not (A or B or not C)


if __name__ == '__main__':
    TableOfTruth(f).draw()
