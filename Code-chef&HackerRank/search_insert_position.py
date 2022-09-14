class Solution:
    def searchInsert(self, arr, target):
        left = 0
        right = len(arr) - 1

        while left <= right:
            mid = (left + right) // 2
            if target > arr[mid]:
                left = mid + 1
            elif target < arr[mid]:
                right = mid - 1
            else:
                return mid

        if target < arr[mid]:
            return mid
        return mid + 1


nums = [1, 3, 5, 6]
target = 7
new_sol = Solution()
print(new_sol.searchInsert(nums, target))
