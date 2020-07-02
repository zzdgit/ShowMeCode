# coding: utf-8

class None:
    def __init__(data, next=None):
        self.data = data
        self.next = next
    
    def rev(head):
        p = head
        cur = head.next
        p.next = None
        while cur:
            tmp = cur.next
            cur.next = p
            p = cur
            cur = tmp
        return p
        
  
if "__name__" == __main__:
    link = Node(1, Node(2, Node(3, Node(4, Node(5, Node(6, Node(7, Node(8, Node(9)))))))))
    root = rev(link)
    while root:
        print(root.data)
        root =root.next