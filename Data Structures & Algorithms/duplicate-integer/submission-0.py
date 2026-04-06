class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        flag = False
        nums = sorted(nums)
        print(nums)
        for i in range(1, len(nums)):
            if nums[i-1]==nums[i]:
                flag = True
                break
        return flag

s = Solution()
nums = [1, 2, 3, 4]
output = s.hasDuplicate(nums)
print(output)
                

        