
# Here don't need to reverse the ans

arr = [1,3,4,2]         # o/p - [-1,-1,-1,4]
n = len(arr)
ans = []
stk = []
for i in range(0,n):
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
print(ans)