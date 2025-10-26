class Node:
    def __init__(self, key, value, freq = None):
        self.key = key
        self.val = value
        self.freq  = freq
        self.prev = None
        self.next = None

class DLL:
    def __init__(self):
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0
    
    def size(self):
        return self.size
    
    def tail(self):
        return self.tail
    
    def head(self):
        return self.head
    
    def insert(self, node):
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node
        node.prev = self.head
        self.size += 1

    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        self.size -= 1

class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.min_freq = float('inf')
        self.node_map = {}
        self.node_array = {}

    def get(self, key: int) -> int:
        if key not in self.node_map:
            return -1

        # Step 1: Get Node Address
        node = self.node_map[key]

        # Step 2: Remove Node From The Current DLL 
        curr_dll = self.node_array[node.freq]
        curr_dll.remove(node)

        # Step 3: Update min freq if conditions are meet
        if curr_dll.size == 0 and self.min == node.freq:
            self.min =  node.freq + 1
        
        # Step 4: Update the node frequency
        node.freq = node.freq + 1
        
        # Step 5: Check if there is a DLL and the new 
        # frequency and create one if it is not present
        if node.freq not in self.node_array:
            self.node_array[node.freq] = DLL()
        
        # Step 6: Add the node to the update frequency - DLL
        new_dll = self.node_array[node.freq]
        new_dll.insert(node)

        # Step 7: Return Node value
        return node.val



    def put(self, key: int, value: int) -> None:
        if key in self.node_map:
            # Step 1: Get Node Address
            node = self.node_map[key]

            # Step 2: Remove Node From The Current DLL 
            curr_dll = self.node_array[node.freq]
            curr_dll.remove(node)

            # Step 3: Update min freq if conditions are meet
            if curr_dll.size == 0 and self.min == node.freq:
                self.min =  node.freq + 1
            
            # Step 4: Update the node frequency and the node value
            node.freq = node.freq + 1
            node.val = value
        
            # Step 5: Check if there is a DLL at the new 
            # frequency and create one if it is not present
            if node.freq not in self.node_array:
                self.node_array[node.freq] = DLL()
            
            # Step 6: Add the node to the update frequency - DLL
            new_dll = self.node_array[node.freq]
            new_dll.insert(node)

        else:  
            # Step 1: Check if capacity is already reached and remove
            # last node in the minimum frequency DLL         
            if len(self.node_map) == self.capacity:
                dll = self.node_array[self.min]
                node = dll.tail.prev
                dll.remove(node)
                del self.node_map[node.key]

            # Step 2: Create a new Node
            node = Node(key, value, 1)

            # Step 3: Check if there is a DLL at the new 
            # frequency and create one if it is not present
            if node.freq not in self.node_array:
                self.node_array[node.freq] = DLL()
            
            #Step 4: Add the node to the DLL at the freq 1
            dll = self.node_array[node.freq]
            dll.insert(node)
            self.min = 1
            self.node_map[key] = node

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)