class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        hash_map = {}
        ans = []

        for str in strs:
            sorted_str = "".join(sorted(str))
            if sorted_str in hash_map:
                group_id = hash_map[sorted_str]
                ans[group_id].append(str)
            else:
                group_id = len(hash_map)
                hash_map[sorted_str] = group_id
                ans.append([str])
        
        return ans
            
        