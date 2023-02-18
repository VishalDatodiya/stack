

arr = [4,5,2,10,8]         # o/p - [-1, 4, -1, 2, 2]
n = len(arr)
ans = []
stk = []
for i in range(0,n):
    while stk:
        if arr[i] <= stk[-1]:
            stk.pop()
        else:
            break
    
    if len(stk) == 0:
        ans.append(-1)
    else:
        ans.append(stk[-1])
    stk.append(arr[i])
print(ans)