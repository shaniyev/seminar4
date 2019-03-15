class Node(object):
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None

    def insert(self, data):
        ''' For inserting the data in the Tree '''
        if self.data == data:
            return False        # As BST cannot contain duplicate data

        elif data < self.data:
            ''' Data less than the root data is placed to the left of the root '''
            if self.leftChild:
                return self.leftChild.insert(data)
            else:
                self.leftChild = Node(data)
                return True

        else:
            ''' Data greater than the root data is placed to the right of the root '''
            if self.rightChild:
                return self.rightChild.insert(data)
            else:
                self.rightChild = Node(data)
                return True

    def minValueNode(self, node):
        current = node

        # loop down to find the leftmost leaf
        while(current.leftChild is not None):
            current = current.leftChild

        return current

    def delete(self, data):
        ''' For deleting the node '''
        if self is None:
            return None

        # if current node's data is less than that of root node, then only search in left subtree else right subtree
        if data < self.data:
            self.leftChild = self.leftChild.delete(data)
        elif data > self.data:
            self.rightChild = self.rightChild.delete(data)
        else:
            # deleting node with one child
            if self.leftChild is None:
                temp = self.rightChild
                self = None
                return temp
            elif self.rightChild is None:
                temp = self.leftChild
                self = None
                return temp

            # deleting node with two children
            # first get the inorder successor
            temp = self.minValueNode(self.rightChild)
            self.data = temp.data
            self.rightChild = self.rightChild.delete(temp.data)

        return self

    def find(self, data):
        ''' This function checks whether the specified data is in tree or not '''
        if(data == self.data):
            return True
        elif(data < self.data):
            if self.leftChild:
                return self.leftChild.find(data)
            else:
                return False
        else:
            if self.rightChild:
                return self.rightChild.find(data)
            else:
                return False

    def preorder(self):
        '''For preorder traversal of the BST '''
        if self:
            print(str(self.data), end = ' ')
            if self.leftChild:
                self.leftChild.preorder()
            if self.rightChild:
                self.rightChild.preorder()

    def inorder(self):
        ''' For Inorder traversal of the BST '''
        if self:
            if self.leftChild:
                self.leftChild.inorder()
            print(str(self.data), end = ' ')
            if self.rightChild:
                self.rightChild.inorder()

    def postorder(self):
        ''' For postorder traversal of the BST '''
        if self:
            if self.leftChild:
                self.leftChild.postorder()
            if self.rightChild:
                self.rightChild.postorder()
            print(str(self.data), end = ' ')

    def less(self, string1, string2):
	    for idx in range(min(len(string1), len(string2))):
	        ordinal1, ordinal2 = ord(string1[idx]), ord(string2[idx])
	        if ordinal1 == ordinal2:
	            continue
	        elif ordinal1 < ordinal2:
	            return True
	        else:
	            return False
	    return len(string1) < len(string2)

class Tree(object):
    def __init__(self):
        self.root = None
        self.size = 0
        self.minValue = None
        self.maxValue = None

    def insert(self, data):
        if self.root and self.root.find(data):
            return
        if self.root:
            self.root.insert(data)
        else:
            self.root = Node(data)
        self.size += 1 
        if self.minValue is None:
        	self.minValue = data
        else:
        	if self.root.less(data, self.minValue):
        		self.minValue = data
        if self.maxValue is None:
        	self.maxValue = data
        else:
        	if not self.root.less(data, self.maxValue):
        		self.maxValue = data



    def delete(self, data):
        self.size -= 1
        if self.root is not None:
            return self.root.delete(data)

    def find(self, data):
        if self.root:
            return self.root.find(data)
        else:
            return False

    def preorder(self):
        if self.root is not None:
            print()
            print('Preorder: ')
            self.root.preorder()

    def inorder(self):
        print()
        if self.root is not None:
            print('Inorder: ')
            self.root.inorder()

    def postorder(self):
        print()
        if self.root is not None:
            print('Postorder: ')
            self.root.postorder()

    def length(self):
    	return self.size

    def min_value(self):
    	return self.minValue

    def max_value(self):
    	return self.maxValue


