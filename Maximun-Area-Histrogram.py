# Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.

# Example 1:

# Input: heights = [2,1,5,6,2,3]
# Output: 10



arr = [6,2,5,4,5,1,6]       # o/p - 12    [5,4,5]  (3 * 4)
n = len(arr)

nsr = []
stk = []

for i in range(n-1,-1,-1):
    while stk and stk[-1][0] >= arr[i]:
       stk.pop()
    if len(stk) == 0:
        nsr.append(n)
    else:
        nsr.append(stk[-1][1])
    stk.append([arr[i],i])
nsr = nsr[::-1] 

nsl = []
stk = []

for i in range(n):
    while stk and stk[-1][0] >= arr[i]:
       stk.pop()
    if len(stk) == 0:
        nsl.append(-1)
    else:
        nsl.append(stk[-1][1])
    stk.append([arr[i],i])
    
print(nsr)
print(nsl)

# width = []
# for i in range(n):
#     ans = nsr[i] - nsl[i] - 1
#     ans = ans * arr[i]
#     width.append(ans)

# print(width)

ans = -1
for i in range(n):
    width = nsr[i] - nsl[i] - 1
    width = width * arr[i]
    ans = max(width, ans)
print(ans)
