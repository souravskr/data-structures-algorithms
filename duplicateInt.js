const nums = [1,2,3,4]

const containsDuplicate = nums => {
    let filtered = nums.filter(num => num >= - (10 ** 9) && num <= (10 ** 9))
    if (filtered.length >= 1 || filtered.length <= (10 ** 5)) {
        const numsSet = new Set(filtered)
        if (filtered.length != numsSet.size) {
            return true
    }
        return false
    }
    
}

console.log(containsDuplicate(nums))



