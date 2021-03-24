class Solution:
    def search(self, inputArr: List[int], target: int) -> int:
        minValue = min(inputArr)
        maxValue = max(inputArr)
        firstElem = inputArr[0]
        lastElem = inputArr[len(inputArr) - 1]

        if(target <= lastElem):
            left_pointer = inputArr.index(minValue)
            right_pointer = len(inputArr) - 1

            while(left_pointer <= right_pointer):
                mid_pointer = int((left_pointer + right_pointer)/2)
                if (target == inputArr[mid_pointer]):
                    return mid_pointer
                elif (target > inputArr[mid_pointer]):
                    left_pointer = mid_pointer + 1
                else:
                    right_pointer = mid_pointer - 1

        else:
            left_pointer = 0
            right_pointer = inputArr.index(maxValue)
            while(left_pointer <= right_pointer):
                mid_pointer = int((left_pointer + right_pointer)/2)
                if (target == inputArr[mid_pointer]):
                    return mid_pointer
                elif (target > inputArr[mid_pointer]):
                    left_pointer = mid_pointer + 1
                else:
                    right_pointer = mid_pointer - 1

        return -1
        