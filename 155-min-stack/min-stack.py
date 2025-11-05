class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack_tracker = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min_stack_tracker or val <=  self.min_stack_tracker[-1]:
            self.min_stack_tracker.append(val)

    def pop(self) -> None:
        if self.stack[-1] == self.min_stack_tracker[-1]:
            self.min_stack_tracker.pop()
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack_tracker[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()