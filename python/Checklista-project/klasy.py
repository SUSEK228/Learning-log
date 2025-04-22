class Task:
    def __init__(self,description):
        self.description=description
        self.done=False
    def do_it(self):
        self.done=True
    def un_do_it(self):
        self.done = False
    def __str__(self):
        status = "[x]" if self.done else "[ ]"
        return f"{status} {self.description}"