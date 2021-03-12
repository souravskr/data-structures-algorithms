const nums = [0,1,0,3,12];

// Take more operation by looking into every item in the array. (Not efficient)
const moveZeros1 = (nums)=> {
    if (nums.length >= 1 || nums.length <= (10 ** 4)){
        nums.forEach(item => {
            if (item === 0 || item > 0x7FFFFFFF) {
                let temp = 0;
                nums.splice(nums.indexOf(item), 1)
                nums.push(temp)
            }
        });
        return nums;
    }
    return nums
}
// Another method using While loop not looking into every item in the array.
const moveZeros = nums =>{
    if (nums.length >= 1 || nums.length <= (10 ** 4)){
        const arrayZero = []
        let countZero = nums.indexOf(0);
        while (countZero != -1) {
            nums.splice(countZero, 1)
            countZero = nums.indexOf(0)
            arrayZero.push(0)
        }
        // push method is more faster than concat
        // return nums.concat(arrayZero)
        nums.push(...arrayZero)
    }

    return nums
    
}





console.log(moveZeros(nums))