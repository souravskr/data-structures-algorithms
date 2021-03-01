// Question is : Write a function that reverse a string


const inputString = "Hello there!"
let outputString = "";


for (let index = inputString.length -1; index >= 0; index--) {
    outputString = outputString.concat(inputString[index]);
}

console.log(outputString)