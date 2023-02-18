

arr = [1,3,4,2]         # o/p - [3, 4, -1, -1]
n = len(arr)
ans = []
stk = []
for i in range(n-1,-1,-1):
    while stk:
        if arr[i] >= stk[-1]:
            stk.pop()
        else:
            break
    
    if len(stk) == 0:
        ans.append(-1)
    else:
        ans.append(stk[-1])
    stk.append(arr[i])
print(ans[::-1])