const inputNum = -123;

// Solution with number to string conversion

const reverseStr = (inputNum)=>{

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

// Soluiton by calculating reminder

const reverse = (inputNum)=> {
    let reminder = 0;
    let sum = 0;
    let input = inputNum
    if (inputNum < 0) {
        inputNum = inputNum * -1;
    }

    while (inputNum > 0) {
        reminder = inputNum % 10;
        sum = sum * 10 + reminder
        inputNum = Math.floor(inputNum / 10);
    }
    console.log(sum)

    if (sum > 0x7FFFFFFF) {
        return 0
    }
    if (input < 0) {
        return sum * -1
    }
    return sum

}

// 




// console.log(parseInt(inputStr, 10))



console.log(reverse(1534236469))