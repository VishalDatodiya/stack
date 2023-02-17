
# Stack using Linked list

# Not good Approach

# suppose we append 1 then append 2 then 3 so head is 1 and tail is 3

# push - O(1)
# pop - O(n)   # bcz if we pop then we have to remove it tail should be second last of linked list or stack

# ===================================================================================================================

#                                       Solution        

# ===================================================================================================================

# So we will always give the head to new node or new push

# 1 2 3

# here 3 pointing 2 and 2 pointing 1

# 3 is head

# push - O(1)
# pop - O(1)  # bcz we pop and head = head.next


# (Look carefully the push operation)


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None        

class StackUsingLinkedList:
    def __init__(self):
        self.count = 0
        self.head = None

    def push(self, data):
        node = Node(data)
        if self.head == None:
            self.head = node
        else:
            node.next = self.head
            self.head = node
        self.count += 1
        return
    
    def pop(self):
        if self.isEmpty():
            print("Stack is Empty!")
            return 
        
        x = self.head.data
        self.head = self.head.next
        print("Popped element : ", x)
        self.count -= 1
        return
    
    def top(self):
        if self.isEmpty():
            print("Stack is Empty!")
            return 
        return self.head.data
    
    def isEmpty(self):
        return self.count == 0
        #     return True
        # return False
    
    def size(self):
        return self.count
    
    def show(self):
        cur = self.head
        while cur:
            print(cur.data, end=" ")
            cur = cur.next
        print()
        return 

stk = StackUsingLinkedList()

while True:
    print("1. Push")
    print("2. Pop")
    print("3. Top")
    print("4. IsEmpty")
    print("5. Size")
    print("6. Exit")
    print("7. Show the Stack")
    op = int(input())
    if op == 1:
        data = int(input())
        stk.push(data)
    elif op == 2:
        stk.pop()
    elif op == 3:
        x = stk.top()
        print("Top of stakc is : ",x)
    elif op == 4:
        isEmpty = stk.isEmpty()
        print("Stack is Empty : ", isEmpty)
    elif op == 5:
        size = stk.size()
        print("Stack size is : ", size)
    elif op == 6:
        break
    elif op == 7:
        stk.show()
    else:
        print("Please select valid operation!")    



































