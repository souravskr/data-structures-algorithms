/**
 * @param {string} s
 * @return {number}
 */
const romanToInt = input => {

    const roman = new Map()
    roman.set("I", 1)
    roman.set("IV", 4)
    roman.set("V", 5)
    roman.set("IX", 9)
    roman.set("X", 10)
    roman.set("XL", 40)
    roman.set("L", 50)
    roman.set("XC", 90)
    roman.set("C", 100)
    roman.set("CD", 400)
    roman.set("D", 500)
    roman.set("CM", 900)
    roman.set("M", 1000)

    let sum = 0
    // let newInpt = ""

    for (let i = 0; i < input.length; i++) {
    
    if (i < input.length - 1 && roman.has(input[i] + input[i+1])) {
        let chunk = input[i]+input[i+1]
        sum+=roman.get(chunk)
        // console.log("Inside", i)
        // continue
        i += 1
    }else if(!roman.has(input[i] + input[i+1])){
        sum += roman.get(input[i])
    }
    
}

    return sum

}