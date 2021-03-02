// Question is : Write a function that reverse a string


const inputString = "sr"


const reverseTheString = inputString => {
    if (typeof inputString === 'string' && inputString.length > 1) {
        let outputString = "";
        for (let index = inputString.length -1; index >= 0; index--) {
            outputString = outputString.concat(inputString[index]);
        }
        return outputString;
    }
    return "Invalid Input"
}

console.log(reverseTheString(inputString))