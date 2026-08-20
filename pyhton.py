class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
    
def traversal(head):
    curr_node = head
    while curr_node:
        print(curr_node.data, end=" -> ")
        curr_node = curr_node.next
    print("null")  
    
def delition(head, NodeToDel):
    if head == NodeToDel:
        head = head.next     
        return head
    
    curr_node = head
    while curr_node.next and curr_node.next != NodeToDel:
            curr_node = curr_node.next   
              
    if curr_node.next is None:
        return head
    curr_node.next = curr_node.next.next  
    return head

def insertion(head, newNode, pos):
    if pos == 1:
        newNode.next = head
        head = newNode
        return head
    curr_node = head
    for _ in range(pos - 2):
        if curr_node.next is Node:
            break
        curr_node = curr_node.next
    newNode.next = curr_node.next
    curr_node.next = newNode
    return head
                  
                  
node1 = Node(2)
node2 = Node(5)
node3 = Node(0)
node4 = Node(10)

node1.next = node2
node2.next = node3
node3.next = node4       

traversal(node1)
node1 = delition(node1, node3)
traversal(node1)

newNode = Node(98)

node1 = insertion(node1, newNode, 2)
traversal(node1)