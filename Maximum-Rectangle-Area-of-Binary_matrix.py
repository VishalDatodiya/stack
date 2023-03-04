



class Solution:
    def MAH(self, arr,n):
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

        ans = -1
        for i in range(n):
            width = nsr[i] - nsl[i] - 1
            width = width * arr[i]
            ans = max(width, ans)
        return ans

    def maximalRectangle(self, mat):
        m = len(mat)
        n = len(mat[0])
        ans = -1
        histogram_array = [0] * n
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 1:
                    histogram_array[j] = histogram_array[j] + mat[i][j]
                else:
                    histogram_array[j] = 0
            max_area = self.MAH(histogram_array, n)
            ans = max(ans,max_area)
        return ans
    
obj = Solution()
mat = [[1,0,1,0,0],[1,0,1,1,1],[1,1,1,1,1],[1,0,0,1,0]]

ans = obj.maximalRectangle(mat)
print(ans)



# def MAH(arr,n):
#     nsr = []
#     stk = []
#     for i in range(n-1,-1,-1):
#         while stk and stk[-1][0] >= arr[i]:
#             stk.pop()
#         if len(stk) == 0:
#             nsr.append(n)
#         else:
#             nsr.append(stk[-1][1])
#         stk.append([arr[i],i])
#     nsr = nsr[::-1] 

#     nsl = []
#     stk = []
#     for i in range(n):
#         while stk and stk[-1][0] >= arr[i]:
#             stk.pop()
#         if len(stk) == 0:
#             nsl.append(-1)
#         else:
#             nsl.append(stk[-1][1])
#         stk.append([arr[i],i])

#     ans = -1
#     for i in range(n):
#         width = nsr[i] - nsl[i] - 1
#         width = width * arr[i]
#         ans = max(width, ans)
#     return ans

# # mat = [[0,1,1,0],[1,1,1,1],[1,1,1,1],[1,1,0,0]]
# # mat = [[1,0,1,0,0],[1,0,1,1,1],[1,1,1,1,1],[1,0,0,1,0]]
# mat = [[1]]
# m = len(mat)
# n = len(mat[0])
# ans = -1
# histogram_array = [0] * n
# for i in range(m):
#     for j in range(n):
#         if mat[i][j] == 1:
#             histogram_array[j] = histogram_array[j] + mat[i][j]
#         else:
#             histogram_array[j] = 0
#     max_area = MAH(histogram_array, n)
#     ans = max(ans,max_area)
# print(ans)

