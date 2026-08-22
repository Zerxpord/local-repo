class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
class Doubly_Linked_List:
    def __init__(self):
        self.head = None
        
    def Traversal(self):
        curr = self.head
        print("null")
        while curr:
            print(f" <-- {curr.data} --> ", end="  ")
            curr = curr.next
        print("null")
    
    def Create_List(self, val):
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
        
        else:
            curr = self.head
            while curr.next is not None:
                curr = curr.next
            curr.next = new_node
            new_node.prev = curr  
            new_node.next = None  
                         
                       
obj = Doubly_Linked_List()
Node1 = obj.Create_List(3)
obj.Create_List(12)
obj.Create_List(5)
obj.Create_List(9)                       
obj.Create_List(0)
obj.Create_List(13)

obj.Traversal()