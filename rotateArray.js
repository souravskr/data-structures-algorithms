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


const rotate = (nums, k)=> {

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

console.log(nums)

for (let i = 0; i < k; i++) {
    const temp = nums[i];
    console.log(temp)
    nums[i] = nums[k-i-1]
    nums[k-i-1] = temp
}

console.log(nums)


// console.log(rotate(nums, k))