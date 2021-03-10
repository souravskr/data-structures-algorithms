const inputNum = -123;

const reverse = (inputNum)=>{

    const inputStr = inputNum.toString();
    const lastIndex = inputStr.length -1;
    let outputStr = "";
    for (let index = lastIndex; index >= 0 ; index--) {
        outputStr = outputStr.concat(inputStr[index])
    }

    if (parseInt(outputStr, 10) > 0x7FFFFFFF) return 0;


    if (inputNum < 0) {
        return parseInt(outputStr, 10) * -1
    }

    return parseInt(outputStr, 10)

}






// console.log(parseInt(inputStr, 10))



console.log(reverse(-1534236469))