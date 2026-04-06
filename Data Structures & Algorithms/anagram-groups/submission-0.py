class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        temp_dict = {}
        list1 = []
        for i in strs:
            key = "".join(sorted(i))
            if key in temp_dict:
                temp_dict[key].append(i)
            else:
                temp_dict[key] = [i]
        return list(temp_dict.values())