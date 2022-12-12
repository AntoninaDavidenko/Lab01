class Node:
    def __init__(self, product_code, price):
        self.product_code = product_code
        self.price = price
        self.leftChild = None
        self.rightChild = None

    def insert(self, product_code, price):
        # if value is lesser than the value of the parent node
        if product_code < self.product_code:
            if self.leftChild:
                # if we still need to move towards the left subtree
                self.leftChild.insert(product_code, price)
            else:
                self.leftChild = Node(product_code, price)
                return
        # if value is greater than the value of the parent node
        else:
            if self.rightChild:
                # if we still need to move towards the right subtree
                self.rightChild.insert(product_code, price)
            else:
                self.rightChild = Node(product_code, price)
                return

    def findval(self, product_code, amount):
        if product_code < self.product_code:
            if self.leftChild is None:
                return str(product_code) + " Not Found"
            return self.leftChild.findval(product_code, amount)
        elif product_code > self.product_code:
            if self.rightChild is None:
                return str(product_code) + " Not Found"
            return self.rightChild.findval(product_code, amount)
        else:
            print(str(self.product_code) + ' is found')
            print("Total price:", amount * self.price)

    def PrintTree(self):
        if self.leftChild:
            self.leftChild.PrintTree()
        print(self.product_code, self.price),
        if self.rightChild:
            self.rightChild.PrintTree()


# Creating root node
root = Node(1, 9)
# Inserting values in BST
root.insert(2, 4)
root.insert(3, 1)
root.insert(5, 19)
root.insert(7, 911)
root.insert(6, 99)
# printing BST
root.PrintTree()
root.findval(2, 4)
