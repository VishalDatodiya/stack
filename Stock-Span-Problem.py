arr = [100,80,60,70,60,75,85]
# arr = [1,2,3,4,5]
n = len(arr)
ans = []
stk = []

# 1. 

# for i in range(n):
#     while stk:
#         if stk[-1][0] <= arr[i]:
#             stk.pop()
#         else:
#             break
#     if len(stk) == 0:
#         ans.append(i+1)
#     else:
#         ans.append(i - stk[-1][1])
#     stk.append([arr[i], i])
# print(ans)


# 2. 

for i in range(n):
    x = 1
    while stk and stk[-1][0] <= arr[i]:
        x += stk.pop()[1]
    ans.append(x)
    stk.append([arr[i],x])

print(ans)
