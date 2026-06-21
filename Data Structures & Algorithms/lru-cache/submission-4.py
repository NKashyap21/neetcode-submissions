class Node:
    def __init__(self,val,next=None,prev=None):
        self.val = val
        self.next = next
        self.prev = prev

class LRUCache:

    def __init__(self, capacity: int):
        self.myHash = {}
        self.head,self.tail = Node(0),Node(0)
        self.head.next = self.tail
        self.tail.prev = self.head

        self.cap = capacity
        self.count = 0

    def get(self, key: int) -> int:
        
        node = self.myHash.get(key,-1)
        if node == -1:
            return -1
        
        node.prev.next = node.next
        node.next.prev = node.prev

        self.tail.prev.next = node
        node.prev = self.tail.prev
        self.tail.prev = node
        node.next = self.tail

        return node.val[-1]

    def put(self, key: int, value: int) -> None:

        node = self.myHash.get(key,-1)
        if node == -1:
            new_node = Node(val=[key,value])
            self.count +=1 
            if self.count > self.cap:
                head_node = self.head.next
                self.head.next = head_node.next
                head_node.next.prev = self.head
                self.myHash.pop(head_node.val[0],None)
                self.count -=1

                self.tail.prev.next = new_node
                new_node.prev = self.tail.prev
                self.tail.prev = new_node
                new_node.next = self.tail

                self.myHash[key] = new_node
            else:
                self.tail.prev.next = new_node
                new_node.prev = self.tail.prev
                self.tail.prev = new_node
                new_node.next = self.tail
                self.myHash[key] = new_node
        else:
            node.val[-1] = value
            node.prev.next = node.next
            node.next.prev = node.prev

            self.tail.prev.next = node
            node.prev = self.tail.prev
            self.tail.prev = node
            node.next = self.tail
        
        
        
