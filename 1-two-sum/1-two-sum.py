class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        copy_numbers = nums.copy()
        nums.sort()

        left_pointer = 0
        right_pointer = len(nums) - 1

        output = []

        for i in range(len(nums)):
            two_sum = nums[left_pointer] + nums[right_pointer]
            if two_sum > target:
                right_pointer -= 1
            elif two_sum < target:
                left_pointer += 1
            else:
                if nums[left_pointer] == nums[right_pointer]:
                    output.append(copy_numbers.index(nums[left_pointer]))
                    output.append(copy_numbers.index(nums[right_pointer], left_pointer + 1))
                    break
                else:
                    output.append(copy_numbers.index(nums[left_pointer]))
                    output.append(copy_numbers.index(nums[right_pointer]))
                    break
        return output