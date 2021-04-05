import math

class Console(object):
    """docstring for Console"""
    def __init__(self, max_lines=20, header=""):
        super(Console, self).__init__()
        self.lines = []
        self.max = max_lines
        self.line_header = header

    def print(self, s):
        l = "{}{}".format(self.line_header, s)
        self.lines.append(l)
        if len(self.lines) > self.max:
            self.lines = self.lines[1:]