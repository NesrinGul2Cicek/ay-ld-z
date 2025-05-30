class Node:
    def __init__(self, pos, g=0, h=0, parent=None):
        self.pos = pos
        self.g = g
        self.h = h
        self.f = g + h
        self.parent = parent

    def __lt__(self, other):
        return self.f < other.f
    
    def __eq__(self, other):
        return isinstance(other, Node) and self.pos == other.pos

    def __hash__(self):
        return hash(self.pos)

