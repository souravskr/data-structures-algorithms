/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    const nums1 = [...nums]
    nums.sort((a, b)=> a-b)
    const output = []
    
    let left = 0
    let right = nums.length -1
    
    
    
    for (let element = 0; element < nums.length; element++) {
    const item = nums[element]
    let twoSum = nums[left] + nums[right]

    if(target > twoSum){
        // console.log("first " + left, right)
        left ++
    }
    else if (target < twoSum){
        // console.log("second " + left, right)
        right --
    }
    else {
        
        if (nums[left] == nums[right]) {
            output.push(nums1.indexOf(nums[left]), nums1.indexOf(nums[right], left + 1))
            break;
        }
        
        output.push(nums1.indexOf(nums[left]), nums1.indexOf(nums[right]))
        break;
    }

}
    return output;
};