class Node:
    value = ""
    children = []
    
    def __init__(self, val):
        self.value = val

    def setChildren(self, children):
        self.children = children
        