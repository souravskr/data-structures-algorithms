const nums = [0,1,0,3,12];


const moveZeros = (nums)=> {
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



console.log(moveZeros([0]))