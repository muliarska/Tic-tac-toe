"""Represents LinkedBinaryTree"""


class LinkedBinaryTree:
    """Represents LinkedBinaryTree"""
    def __init__(self, root):
        """
        () ->
        Initialize LinkedBinaryTree"""
        self.key = root
        self.left_child = None
        self.right_child = None

    def insert_left(self, new_node):
        """Inserts element in a left side of the tree"""
        if self.left_child is None:
            self.left_child = LinkedBinaryTree(new_node)
        else:
            treee = LinkedBinaryTree(new_node)
            treee.left_child = self.left_child
            self.left_child = treee

    def insert_right(self, new_node):
        """Inserts element in a right side of the tree"""
        if self.right_child is None:
            self.right_child = LinkedBinaryTree(new_node)
        else:
            treee = LinkedBinaryTree(new_node)
            treee.right_child = self.right_child
            self.right_child = treee

    def get_right_child(self):
        """Returns right child of the tree"""
        return self.right_child

    def get_left_child(self):
        """Returns left child of the tree"""
        return self.left_child

    def set_root_val(self, obj):
        """Sets root value"""
        self.key = obj

    def get_root_val(self):
        """Returns root value"""
        return self.key

    def preorder(self):
        """Performs preorder for the tree"""
        print(self.key)
        if self.left_child:
            self.left_child.preorder()
        if self.right_child:
            self.right_child.preorder()

    def inorder(self):
        """Performs inorder for the tree"""
        if self.left_child:
            self.left_child.inorder()
        print(self.key)
        if self.right_child:
            self.right_child.inorder()

    def postorder(self):
        """Performs postorder for the tree"""
        if self.left_child:
            self.left_child.postorder()
        if self.right_child:
            self.right_child.postorder()
        print(self.key)
