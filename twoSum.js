let nums = [3,3]
// let num3 = [...nums]

const target = 6
// const output = []


// nums.sort((a, b)=> a-b)


// Brute Force Method ==> Complexity O(n^2)
// nums.forEach(item => {
//     for (let index = 1; index < nums.length; index++) {
        
//         if (item + nums[index] == target){
//             output.push(nums.indexOf(item), index)
//             break;
//         }
//         break;
        
//     }
// })

// console.log(output.sort((a,b)=> a-b))


// ==> Complexity O(n)

// const output1 = []
// const output3 = []
// let left = 0
// let right = nums.length -1


// for (let element = 0; element < nums.length; element++) {
//     const item = nums[element]
//     let twoSum = nums[left] + nums[right]

//     if(target > twoSum){
//         // console.log("first " + left, right)
//         left ++
//     }
//     else if (target < twoSum){
//         // console.log("second " + left, right)
//         right --
//     }
//     else {
//         console.log(nums[left], nums[right])

//         if (nums[left] == nums[right]) {
//             output1.push(num3.indexOf(nums[left]), num3.indexOf(nums[right], left + 1))
//             break;
//         }
//         output1.push(num3.indexOf(nums[left]), num3.indexOf(nums[right]))
        
//         break;
//     }

// }

const twoSum = function(nums, target) {
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




console.log(twoSum(nums, target))