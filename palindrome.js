const inputNum = -123;

// Reverse integer by converting number into string

const isPalindromeByString = (inputNum)=>{

    const inputStr = inputNum.toString();
    const lastIndex = inputStr.length -1;
    let outputStr = "";
    for (let index = lastIndex; index >= 0 ; index--) {
        outputStr = outputStr.concat(inputStr[index])
    }

    if (parseInt(outputStr, 10) > 0x7FFFFFFF) return false;

    return outputStr === inputStr

}
// Solution with reminder

const isPalindrome = (inputNum)=> {
    let reminder = 0;
    let sum = 0;
    let input = inputNum

    while (inputNum > 0) {
        reminder = inputNum % 10;
        sum = sum * 10 + reminder
        inputNum = Math.floor(inputNum / 10);
    }

    if (sum > 0x7FFFFFFF || input != sum) {
        return false
    }
    return true

}



// console.log((12/10).toPrecision(1))


// console.log(parseInt(inputStr, 10))



console.log(isPalindrome(121))