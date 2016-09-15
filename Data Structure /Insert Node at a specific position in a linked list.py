"""
 Insert Node at a specific position in a linked list
 head input could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the head of the linked list in the below method. 
"""
#This is a "method-only" submission.
#You only need to complete this method.
def InsertNth(head, data, position):

    newNode = Node(data)

    if  head == None:
        return newNode

    elif position == 0:
        newNode.next = head
        head = newNode

    elif position == 1:
        newNode.next = head.next
        head.next = newNode

    else:
        head.next = InsertNth(head.next, data, position - 1)

    return head
  
  
  
  
  
  
  
  

