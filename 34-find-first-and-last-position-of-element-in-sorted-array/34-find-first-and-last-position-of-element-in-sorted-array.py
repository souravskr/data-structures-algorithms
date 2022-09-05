class Solution:
    def searchRange(self, arr: List[int], target: int) -> List[int]:
        if target not in arr:
            return [-1, -1]

        target_count = arr.count(target)
        start_index = arr.index(target)
        last_index = start_index + target_count - 1
        return [start_index, last_index]