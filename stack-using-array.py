
# stack using array


# arr = []

# for i in range(1,6):
#     arr.append(i)
    
# print(arr)
# for i in range(len(arr)):
#     print(arr.pop())        # 5 4 3 2 1
    
    

# Stack using Array
    
class Stack:
    def __init__(self):
        self.stk_size = 0
        self.arr = []

    def push(self, data):
        self.arr.append(data)
        self.stk_size += 1
        return
    
    def pop(self):
        if self.isEmpty():
            print("Stack is Empty!")
            return 
        print("Popped element : ", self.arr.pop())
        self.stk_size -= 1
        return
    
    def top(self):
        if self.isEmpty():
            print("Stack is Empty!")
            return 
        return self.arr[-1]
    
    def isEmpty(self):
        if self.stk_size == 0:
            return True
        return False
    
    def size(self):
        return self.stk_size
    
    def show(self):
        print(self.arr)
        return


stk = Stack()

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


        





