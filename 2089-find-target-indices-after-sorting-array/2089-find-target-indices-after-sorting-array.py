class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        if target not in nums:
            return []
        
        nums.sort()
        
        count_target = nums.count(target)
        first_index = nums.index(target)
        if count_target > 1:
            last_index = first_index + count_target - 1
            return [i for i in range(first_index, last_index + 1)]
        
        return [first_index]