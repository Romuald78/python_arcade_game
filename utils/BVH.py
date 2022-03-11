
IDX_VALUE = 0
IDX_DATA  = 1
IDX_LEFT  = 2
IDX_RIGHT = 3
IDX_PREV  = 4

class BST():

    def __init__(self):
        self.tree = None

    # - numeric value to be compared to
    # - data object
    # - pointer to left subtree
    # - pointer to right subtree
    def __createNode(self, data, value):
        node = [value, data, None, None]
        return node

    def __addNode(self, current, data, value):
        if current is None:
            return self.__createNode(data, value)
        elif value <= current[IDX_VALUE]:
            current[IDX_LEFT] = self.__addNode(current[IDX_LEFT], data, value)
            return current
        else:
            current[IDX_RIGHT] =  self.__addNode(current[IDX_RIGHT], data, value)
            return current

    def addNode(self, data, value):
        self.tree = self.__addNode(self.tree, data, value)

    def __getStr(self, current):
        res = ''
        if current is not None:
            res += self.__getStr( current[IDX_LEFT] )
            res += f"{current[IDX_VALUE]} \n"
            res += self.__getStr( current[IDX_RIGHT] )
        return res

    def __str__(self):
        return self.__getStr(self.tree)

bst = BST()

for i in range(10):
    bst.addNode(None, i)

print( bst )


