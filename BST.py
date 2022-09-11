from turtle import right


class BST:
    NODE_WIDTH = 2
    def __init__(self, key):
        self.key = key
        self.right = None
        self.left = None
        self.width = BST.NODE_WIDTH
        self.height = 0
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
        self.update_height()
        self.update_width()

    def update_height(self):
        right_height = -1
        left_height = -1
        if self.left is not None:
            left_height = self.left.height
        if self.right is not None:
            right_height = self.right.height
        self.height = 1 + max(right_height, left_height)

    def update_width(self):
        total = BST.NODE_WIDTH
        if self.left is not None:
            total += self.left.width
        if self.right is not None:
            total +=  self.right.width
        self.width = total

    def draw(self):
        q = [(0, self.compute_pos(0),self)]
        
        total_str = ""
        while len(q) > 0:
            newq = []
            current_line = ""
            for start,pos, node in q:
                if node.left is not None:
                    left_child_pos = node.left.compute_pos(start)
                    newq.append((start, left_child_pos,node.left))

                    current_line += (left_child_pos - len(current_line)) * " "
                    current_line += (pos - len(current_line)) * "_"
                current_line += (pos - len(current_line))*" "
                current_line += node.zeropad()
                if node.right is not None:
                    right_start = pos+BST.NODE_WIDTH
                    right_child_pos = node.right.compute_pos(right_start)
                    newq.append((right_start,right_child_pos,node.right))
                    current_line += (right_child_pos - len(current_line) + BST.NODE_WIDTH) * "_"
            q = newq
            total_str += current_line + "\n"
        return total_str


    def compute_pos(self,start):
        pos = start
        if self.left is not None:
            pos += self.left.width
        return pos


    def zeropad(self):
        if self.key < 10:
            return "0" + str(self.key)
        return str(self.key)



                

tree = BST(5)
tree.insert(3)
tree.insert(2)
tree.insert(4)
tree.insert(13)
tree.insert(19)
tree.insert(10)
tree.insert(8)
tree.insert(12)


print(tree.draw())


   
