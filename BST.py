from turtle import left, right


class BST:
    def __init__(self, key):
        self.key = key
        self.right = None
        self.left = None
        self.width = len(str(key))
        self.height = 0
        self.l = LNode(key)
    def insert(self, key):
        
        if key < self.key:
            if self.left is None:
                self.left = BST(key)
                successor = self.l
                new_node = self.left.l
                predecessor = successor.prev
                if predecessor is not None:
                    predecessor.next = new_node
                new_node.prev = predecessor
                new_node.next = successor
                successor.prev = new_node
            else:
                self.left = self.left.insert(key)
        elif key > self.key:
            if self.right is None:
                self.right = BST(key)
                predecessor = self.l
                new_node = self.right.l
                successor = predecessor.next
                if successor is not None:
                    successor.prev = new_node
                new_node.prev = predecessor
                new_node.next = successor
                predecessor.next = new_node
            else:
                self.right = self.right.insert(key)
                
        self.update_height()
        
        root = self.rebalance()
        root.update_width()
        self.update_width()
        
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
        total = len(str(self.key))
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
                current_line += str(node.key)
                if node.right is not None:
                    right_start = pos+len(str(node.key))
                    right_child_pos = node.right.compute_pos(right_start)
                    newq.append((right_start,right_child_pos,node.right))
                    current_line += (right_child_pos - len(current_line) + len(str(node.right.key)) ) * "_"
            q = newq
            total_str += current_line + "\n"
        return total_str

    def linked_list(self):
        smallest = self
        while smallest.left is not None:
            smallest = smallest.left
        head = smallest.l
        ordered = []
        while head is not None:
            ordered.append(head.key)
            head = head.next
        return ordered

    def compute_pos(self,start):
        pos = start
        if self.left is not None:
            pos += self.left.width
        return pos

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
    
    def __iter__(self):
        smallest = self
        while smallest.left is not None:
            smallest = smallest.left
        head = smallest.l
        return head.__iter__()


        

class LNode:
    def __init__(self,key):
        self.key = key
        self.next = None
        self.prev = None
    def __iter__(self):
        current = self
        while current is not None:
            yield current.key
            current = current.next

class Tree:
    def __init__(self):
        self.t = None

    def insert(self, key):
        if self.t is None:
            self.t = BST(key)
        else:
            self.t = self.t.insert(key)
    def print_tree(self):
        return self.t.draw()
    def print_list(self):
        return self.t.linked_list()
    def __iter__(self):
        return self.t.__iter__()

                

# tree = Tree()
# tree.insert(5)
# tree.insert(1)
# tree.insert(3)
# tree.insert(2)
# tree.insert(4)
# tree.insert(13)
# tree.insert(19)
# tree.insert(20)
# tree.insert(10)
# tree.insert(8)
# tree.insert(12)
# tree.insert(9)
# tree.insert(21)

# tree.insert(22)

# tree.insert(23)
# tree.insert(24)
# tree.insert(25)

# print(tree.print_tree())



def func():
    return 3
    if False:
        yield 3
print([item for item in func()])
print(func())