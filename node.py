class Node:

    #czy przechowuje znak
    def isLeaf(self):
        return self.character != ""

    def __init__(self, value=0, character="", right=None, left=None):
        self.value = value
        self.character = character
        self.right = right
        self.left = left

    #https://www.pythonpool.com/python-__lt__/
    def __lt__(self, other):
        if self.value != other.value:  #jezeli liscie sa rozne
            return self.value < other.value
        if not self.isLeaf() and other.isLeaf():  #jezeli maja znak
            return True
        if self.isLeaf() and not other.isLeaf():
            return False
        if self.isLeaf() and other.isLeaf():  # oba maja to kolejnosc alfabetyczna
            return ord(self.character[0]) < ord(other.character[0])
        return True
