import pdb
class Node:
    """
    Represents a node in a linked list.
    """
    def __init__(self,data):
        self.data = data    # Store the data
        self.next = None    # Initialize next as None


class LinkedList:
    """
    Represents a singly linked list.
    """

    def __init__(self):
        self.head = None    # Initialize the head of the list



    def append(self,data):
        """
        Add a new node to the end of the linked list.
        :param data: Data to be added to the node.
        """
        #pdb.set_trace()

        new_node = Node(data)
        if not self.head:   # If the list is empty, set the new node as head
            print(f"Old head value is {self.head}")
            self.head = new_node
            print(f"New head value is {self.head}")
            return
        # Traverse to the end of the list and add the new node
        current = self.head
        print(f"The value of current is {current}")
        print(f"The value of next current is {current.next}")
        while current.next:
            current = current.next
        current.next = new_node

    def display(self):
        """
        Print the linked list elements.
        """
        #pdb.set_trace()
        current = self.head
        while current:
            print(current.data,end = " -> ")
            current = current.next
        print("None")

ll = LinkedList()
ll.append(10)
ll.append(20)
ll.display()
