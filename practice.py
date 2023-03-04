# NGR
# NGL
# NSR
# NSL

# arr = [1,3,2,5]
# n = len(arr)
# ans = []
# stk = []
# for i in range(n-1,-1,-1):
#     while stk and stk[-1] <= arr[i]:
#         stk.pop()
#     if len(stk) == 0:
#         ans.append(-1)
#     else:
#         ans.append(stk[-1])
#     stk.append(arr[i])
# print(ans[::-1])

# arr = [1,3,2,5]
# n = len(arr)
# ans = []
# stk = []
# for i in range(0,n,1):
#     while stk and stk[-1] <= arr[i]:
#         stk.pop()
#     if len(stk) == 0:
#         ans.append(-1)
#     else:
#         ans.append(stk[-1])
#     stk.append(arr[i])
# print(ans)


# arr = [1,3,2,5]
# n = len(arr)
# ans = []
# stk = []
# for i in range(n-1,-1,-1):
#     while stk and stk[-1] >= arr[i]:
#         stk.pop()
#     if len(stk) == 0:
#         ans.append(-1)
#     else:
#         ans.append(stk[-1])
#     stk.append(arr[i])
# print(ans[::-1])

# arr = [1,3,2,5]
# n = len(arr)
# ans = []
# stk = []
# for i in range(0,n,1):
#     while stk and stk[-1] >= arr[i]:
#         stk.pop()
#     if len(stk) == 0:
#         ans.append(-1)
#     else:
#         ans.append(stk[-1])
#     stk.append(arr[i])
# print(ans)


# arr = [100,80,60,70,60,75,85]
# arr = [1,2,3,4,5]
# n = len(arr)
# ans = []
# stk = []
# for i in range(n):
#     while stk and stk[-1][0] <= arr[i]:
#         stk.pop()
#     if len(stk) == 0:
#         ans.append(i+1)
#     else:
#         ans.append(i-stk[-1][1])
#     stk.append([arr[i],i])
# print(ans)


arr = [1,12,3,4,5]
k = 3
n = len(arr)
i = 0
j = 0
ans = 0
sum = 0
while j < n:
    if (j-i+1) < k:
        sum += arr[j]
    elif (j-i+1) == k:
        sum += arr[j]
        ans = max(ans,sum)
        sum -= arr[i]
        i += 1
    j += 1
print(ans)