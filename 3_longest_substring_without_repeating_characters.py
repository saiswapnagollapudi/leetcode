class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 0
        max_length_so_far = 0
        for i in s:
            if i in s[l:r]:
                l = l + s[l:r].index(i) + 1
            r += 1
            max_length_so_far = max(max_length_so_far,r-l)
        return(max_length_so_far)
