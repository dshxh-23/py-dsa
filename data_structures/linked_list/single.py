from core.nodes import Node

class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0           # to allow count operations in O(1) time
        
    def __len__(self):
        return self.count
    
    def __bool__(self):
        return self.head is not None

    def __iter__(self):
        curr = self.head
        while curr:
            yield curr.data
            curr = curr.next

    def __str__(self):
        nodes = [str(data) for data in self]        # casting linked list into a python list
        return " => ".join(nodes) + " => None"
    
    def __repr__(self):
        return f"Node({self.data})"


    ###################


    def prepend(self, val):
        new_node = Node(val)
        self.count += 1

        if not self:
            self.head = new_node
            self.tail = new_node
            return

        new_node.next = self.head
        self.head = new_node


    def append(self, val):
        new_node = Node(val)
        self.count += 1

        if not self:
            self.head = new_node
            self.tail = new_node
            return

        self.tail.next = new_node
        self.tail = new_node 
        

    # IMPLEMENT LATER
    def insert(self, val, index):
        ...

    ##################

    def _empty_list(self):
        """ internal helper to cleanly empty list when it contains only 1 element """

        if not self.count == 1:
            return

        deleted_val = self.head.data

        self.head = None
        self.tail = None
        self.count = 0
        return deleted_val
        

    def popleft(self):
        if not self:
            raise IndexError("popleft from empty list")

        if self.count == 1:
            return self._empty_list()

        pop_val = self.head.data
        self.head = self.head.next
        self.count -= 1
        return pop_val


    def pop(self):
        if not self:
            raise IndexError("pop from empty list")

        if self.count == 1:
            return self._empty_list()
        
        pop_val = self.tail.data
        curr = self.head
        while curr.next is not self.tail:
            curr = curr.next
        
        self.tail = curr
        self.tail.next = None
        self.count -= 1
        return pop_val
    
    
    def remove(self, val, all=False):
        if not self:
            return False
        
        prev = None
        curr = self.head
        removed = False

        while curr:
            if curr.data == val:
                removed = True

                if curr == self.head:
                    self.popleft()
                    curr = self.head

                elif curr == self.tail:
                    self.pop()
                    curr = None

                else:
                    prev.next = curr.next
                    self.count -= 1
                    curr = curr.next

                if not all:
                    return True
                
            else:
                prev = curr     # Don't need to move prev if value matched!
                curr = curr.next

        return removed

    ##################
    
    def contains(self, val):
        """check if a value exists in a the list: O(n)"""
        return val in self      # works bcz we defined __iter__!
    

    def find(self, val):
        """ 
        returns the index of the first occurance of val in ll.
        returns -1 if val not found
        """
        for index, item in enumerate(self):
            if item == val:
                return index
        return -1

    
    def replace(self, old_val, new_val, all=False):
        """
        replaces the first occurence of old val with new val
        if all is True, replace all occurences of old_val with new_val  
        """
        curr = self.head
        replaced = False

        while curr:
            if curr.data == old_val:
                curr.data = new_val
                replaced = True
            
                if not all:
                    return True
            
            curr = curr.next
            
        return replaced

    
    #=================================================================================================== 


    def detect_cycle(self):
        ...

    def reverse_list(self):
        ...

    def find_middle_node(self):
        ...



#=================================================================================================== 



def main():
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    print(ll)
    
if __name__ == "__main__":
    main()



    
        
