# Consider an array Arr[] = {1, 4, 5, 3, 12, 10}
# For i = 0: stk = {1}
# For i = 1: stk = {1, 4}
# For i = 2: stk = {1, 4, 5}
# For i = 3: stk = {1, 3}  [pop 4 and 5 as 4 > 3 and 5 > 3]
# For i = 4: stk = {1, 3, 12}
# For i = 5: stk = {1, 3, 10} [pop 12 as 12 > 10] 



# We need only increasing / decreasing Value

# arr = [1,4,5,3,12,10]
# o/p = [1,3,10]



# 1. Increasing Monotonic Stack

arr = [1,4,5,3,12,10]
n = len(arr)
stk = []
for i in range(n):
    
    while stk and stk[-1] > arr[i]:
        stk.pop()
    stk.append(arr[i])

print(stk)
    
    
# 2. Monotonic Decreasing Stack

# arr = [1,4,5,3,12,10]
arr = [15,17,12,13,14,10]
n = len(arr)
stk = []
for i in range(n):
    
    while stk and stk[-1] < arr[i]:
        stk.pop()
    stk.append(arr[i])

print(stk)
    
