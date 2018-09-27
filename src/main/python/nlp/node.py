class node():
    def __init__(self, pos):
        self.pos = pos
        self.next = None

    def addNextNode(self, node):
        self.next = node