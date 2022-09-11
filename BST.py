class BST:
    NODE_WIDTH = 2
    def __init__(self, key):
        self.key = key
        self.right = None
        self.left = None
    def insert(self, key):
        if key < self.key:
            if self.left is None:
                self.left = BST(key)
            else:
                self.left.insert(key)
        elif key > self.key:
            if self.right is None:
                self.right = BST(key)
            else:
                self.right.insert(key)
    def width(self):
        total = BST.NODE_WIDTH
        if self.left is not None:
            total += self.left.width()
        if self.right is not None:
            total +=  self.right.width()
        return total
    def visual(self, start):
        width_right = 0
        width_left = 0
        if self.left is not None:
            width_left = self.left.width()
            self.left.visual(start)

        self.pos = start + width_left

        if self.right is not None:
            self.right.visual(self.pos + BST.NODE_WIDTH)


    def zeropad(self):
        if self.key < 10:
            return "0" + str(self.key)
        return str(self.key)


    def draw(level):
        current_string = ""
        for node in level:
            if node.left is not None:
                current_string += (node.left.pos-len(current_string))*" "
                current_string += (node.pos - len(current_string))*"_"
            current_string += (node.pos - len(current_string))*" "

            current_string += node.zeropad()
            if node.right is not None:
                current_string += (node.right.pos - len(current_string) + BST.NODE_WIDTH)*"_"
        return current_string
    def printtree(self):
        q= [self]
        total_str = ""
        while q:
            total_str += BST.draw(q) + "\n"
            new_q  = []
            for node in q:
                if node.left is not None:
                    new_q.append(node.left)
                if node.right is not None:
                    new_q.append(node.right)
            q = new_q
        return total_str


                

tree = BST(5)
tree.insert(3)
tree.insert(2)
tree.insert(4)
tree.insert(13)
tree.insert(19)
tree.insert(10)
tree.insert(8)
tree.insert(12)

tree.visual(0)
print(tree.printtree())


   
