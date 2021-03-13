const nums = [1,2,3,4,5,6,7]
const k = 3


const rotate1 = (nums, k) =>{
    let filtered = nums.filter(num => num >= - (2 ** 31) && num <= (2 ** 31) -1)
    if (filtered.length >= 1 || filtered.length <= (2 ** 10000)) {

        const sliced = filtered.slice(-k)
        const rest = filtered.slice(0, filtered.length - k)
        sliced.push(...rest)
        return sliced
    }
}

// console.log(rotate(nums, k))

const rotate2 = (nums, k)=> {

    nums = nums.filter(num => num >= - (2 ** 31) && num <= (2 ** 31) -1)
    if (nums.length >= 1 || nums.length <= (2 ** 10000)) {
        
        const arrLength = nums.length
    const sliced = []
    for (let item = arrLength -1; item >= arrLength - k; item --) {
        const element = nums[item];
        sliced.push(element)
        nums.pop(element)
    }
    for (let index = 0; index < sliced.length; index++) {
        const element = sliced[index];
        nums.unshift(element)
    }
    return nums
    }
}


const rotate3 = (nums, k)=> {

    nums = nums.filter(num => num >= - (2 ** 31) && num <= (2 ** 31) -1)
    if ((nums.length >= 1 || nums.length <= (2 ** 10000)) && (k >= 0 || k <= (10 ** 5)) ) {

        const newNums = [...nums]
        const arrLength = nums.length
        let l = 1
        while (l <= k) {
            let index = newNums.length - l
            nums.pop(nums[index])
            nums.unshift(newNums[index])
            l++
        }
        return nums

    }
    
}

// nums.reverse()

// Original List                   : 1 2 3 4 5 6 7
// After reversing all numbers     : 7 6 5 4 3 2 1
// After reversing first k numbers : 5 6 7 4 3 2 1
// After revering last n-k numbers : 5 6 7 1 2 3 4 --> Result


const rotate = (nums, k) => {
    const numsLen = nums.length
    k = k % numsLen
    reverse(nums, 0, numsLen -1)
    reverse(nums, 0, k-1)
    return reverse(nums, k, numsLen -1)
}

const reverse = (arr, startIndex, lastIndex)=> {
    let temp = 0;
    while (startIndex < lastIndex) {
        temp = arr[startIndex]
        arr[startIndex] = arr[lastIndex]
        arr[lastIndex] = temp
        startIndex++
        lastIndex--
    }
}

