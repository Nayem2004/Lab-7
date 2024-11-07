#Lab 7

class Node:
    def __init__(self, value=None, next=None, previous=None):
        # Private properties
        self.__value = value
        self.__next = next
        self.__previous = previous
    
    # Sets and gets the Value.
    def set_value(self, value):
        self.__value = value
        return self
    
    def get_value(self):
        return self.__value
    
    # Next Node management.
    def set_next(self, next_node):
        self.__next = next_node
        return self
    
    def get_next(self):
        return self.__next
    
    # Previous Node management.
    def set_previous(self, previous_node):
        self.__previous = previous_node
        return self
    
    def get_previous(self):
        return self.__previous


def main():
    # Creates nodes
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    
    # Links nodes
    node1.set_next(node2)
    node2.set_previous(node1)
    node2.set_next(node3)
    node3.set_previous(node2)
    
    # Displays the linked list from node1 to node3.
    current_node = node1
    while current_node is not None:
        print("Node Value:", current_node.get_value())
        current_node = current_node.get_next()
    
    # Displays the linked list in reverse from node3 to node1.
    current_node = node3
    while current_node is not None:
        print("Node Value (Reverse):", current_node.get_value())
        current_node = current_node.get_previous()


# Calls the main function.
main()
