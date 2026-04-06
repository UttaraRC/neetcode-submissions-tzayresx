class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        value_index_dict = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in value_index_dict:
                return [value_index_dict[complement],i]
            value_index_dict[num] = i
        print(value_index_dict)

solution = Solution()
solution.twoSum([3,4,5,4], 8)



            
        
            
        