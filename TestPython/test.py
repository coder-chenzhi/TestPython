class Solution:
    # @return a tuple, (index1, index2)
    def twoSum(self, num, target):
        start = 1
        end = len(num)
        num.sort()
        
        while (num[start - 1] + num[end - 1] != target):
            if (num[start - 1] + num[end - 1] > target):
                end -= 1
            else:
                start += 1
        
        return sorted((start, end))

s = Solution()
print s.twoSum([3,2,4], 6)