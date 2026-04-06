class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sorted_s = sorted(s)
        sorted_t = sorted(t)
        s_rearange = "".join(sorted_s)
        t_rearange = "".join(sorted_t)
        if s_rearange == t_rearange:
            return True
        else:
            return False

solution = Solution()
s = "racecar"
t = "carrace"
output = solution.isAnagram(s, t)
print(s,t)
        