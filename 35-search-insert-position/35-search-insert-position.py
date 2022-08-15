class Solution:
    def searchInsert(self, arr: List[int], target: int) -> int:
        if target not in arr:
            arr.append(target)
        arr.sort()
        size = len(arr)
        left = 0
        right = size - 1

        while left <= right:
            mid = int((left + right)/2)
            if target == arr[mid]:
                return mid
            elif target < arr[mid]:
                right = mid - 1
            else:
                left = mid + 1
                
        return mid + 1