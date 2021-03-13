/**
 * @param {number[]} nums
 * @param {number} k
 * @return {void} Do not return anything, modify nums in-place instead.
 */
const rotate = (nums, k)=> {

    const numsLen = nums.length
    k = k % numsLen
    reverse(nums, 0, numsLen -1)
    reverse(nums, 0, k-1)
    return reverse(nums, k, numsLen -1)
};


const reverse = (arr, startIndex, lastIndex)=> {
    let temp = 0;
    while (startIndex < lastIndex) {
        temp = arr[startIndex]
        arr[startIndex] = arr[lastIndex]
        arr[lastIndex] = temp
        startIndex++
        lastIndex--
    }
};