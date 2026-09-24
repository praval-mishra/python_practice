# arr=[20,3,5,8,30,10]
# maxi=arr[0]
# for i in arr:
#     if i>maxi:
#         maxi =i
# print(maxi)
# print(max(arr))
# min(arr)
#------------------------------------------------------------
# two sum problem 
# num=[10,2,3,4,5,8,7]
# target=14
# for i in range(len(num)):
#     for j in range(i+1,len(num)) :
#         if num[i]+num[j]==target :
#             print(i,j)
# lets optimize this problem and reduce the time complexity 
# nums = [10, 2, 3, 4, 5, 8, 7]
# target = 9

# seen={}
# for i ,num in enumerate(nums):
#     compliment=target-num
#     if compliment in seen :
#         print([seen[compliment], i])
#         break
#     seen[num]=i 

class Solution(object):
    def twoSum(self, nums, target):
       

        seen = {}  # dictionary to store number:index

        # Loop through list with both index and value
        for i, num in enumerate(nums):
            complement = target - num   # number we need to reach target

            # If complement already seen, return indices
            if complement in seen:
                return [seen[complement], i]

            # Otherwise, store current number with its index
            seen[num] = i
sol=Solution()
nums = [10, 2, 3, 4, 5, 8, 7]
target = 14
print(sol.twoSum(nums, target))
