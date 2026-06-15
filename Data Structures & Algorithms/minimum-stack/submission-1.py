class MinStack:

    def __init__(self):
        self.s1 = []
        self.s2 = []

    def push(self, val: int) -> None:
        self.s1.append(val)
        if len(self.s2) == 0:
            self.s2.append(val)
        elif self.s2[-1] > val:
            self.s2.append(val)
        else:
            self.s2.append(self.s2[-1])

    def pop(self) -> None:
        self.s1.pop()
        self.s2.pop()

    def top(self) -> int:
        return self.s1[-1]

    def getMin(self) -> int:
        return self.s2[-1]
