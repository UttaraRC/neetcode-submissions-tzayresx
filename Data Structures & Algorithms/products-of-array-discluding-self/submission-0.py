import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        for i in range(len(nums)):
            element = nums.pop(i)
            print(element)
            product = math.prod(nums)
            nums.insert(i, element)
        # for i in nums:

        #     if i == 0:
        #         pass
        #     else:
        #         product = int(math.prod(nums)/int(i))
            output.append(product)
        return output