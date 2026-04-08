class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums = sorted(nums)
        dup_list = []
        #create dictionary from list with zero value
        temp_dict = dict.fromkeys(nums, 0)
        print(temp_dict)
        #find frequency of every value in list
        for i in nums:
            temp_dict[i] += 1
    
        print(temp_dict)
        #sorted keys by it's frequency and retun k
        # most frequent elements within the array
        sorted_keys_by_value = sorted(temp_dict, key=temp_dict.get,
        reverse=True)[:k]
        return sorted_keys_by_value

            
        
        # for i in range(1, len(nums)):
        #     if nums[i-1] == nums[i]:
        #         if nums[i] not in dup_list:
        #             dup_list.append(nums[i])
        
            