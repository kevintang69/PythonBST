from turtle import left, right


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
                self.left = self.left.insert(key)
        elif key > self.key:
            if self.right is None:
                self.right = BST(key)
            else:
                self.right = self.right.insert(key)
                
        self.update_height()
        
        root = self.rebalance()
        return root
        
    

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

    def rebalance(self):
        right_height = -1
        left_height = -1
        if self.right is not None:
            right_height = self.right.height
        if self.left is not None:
            left_height = self.left.height
        root = self
        diff = right_height - left_height
        if diff < -1: #left imbalance so right rotate
            left_of_left_height = -1
            right_of_left_height = -1
            if root.left.left is not None:
                left_of_left_height = root.left.left.height
            if root.left.right is not None:
                right_of_left_height = root.left.right.height
            if right_of_left_height > left_of_left_height:
                self.left = self.left.left_rotate()
            root = self.right_rotate()

      
        elif diff > 1:

            left_of_right_height = -1
            right_of_right_height = -1
            if root.right.left is not None:
                left_of_right_height = root.right.left.height
            if root.right.right is not None:
                right_of_right_height = root.right.right.height
            if right_of_right_height < left_of_right_height:
                self.right = self.right.right_rotate()
            root = self.left_rotate()


        
        self.update_width()
        # root.update_width()
        
        return root


    def right_rotate(self):
        right_child_of_left = self.left.right
        root = self.left
        root.right = self
        self.left = right_child_of_left
        self.update_height()
        root.update_height()
        return root
    def left_rotate(self):
        left_child_of_right = self.right.left
        root = self.right
        root.left = self
        self.right = left_child_of_right
        self.update_height()
        root.update_height()
        return root


                

tree = BST(5)
tree = tree.insert(1)
tree = tree.insert(3)
tree = tree.insert(2)
tree = tree.insert(4)
tree = tree.insert(13)
tree = tree.insert(19)
tree = tree.insert(20)
tree = tree.insert(10)
tree = tree.insert(8)
tree = tree.insert(12)





print(tree.draw())


   
