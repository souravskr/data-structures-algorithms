// Question is : Write a function that reverse a string


const inputString = "I'm a student"


const reverTheString = inputString => {
    let outputString = "";
    for (let index = inputString.length -1; index >= 0; index--) {
        outputString = outputString.concat(inputString[index]);
    }
    return outputString;
}

console.log(reverTheString(inputString))