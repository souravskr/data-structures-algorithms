// Create a function that reverse a string:
// 'I'm John' should be: nhoJ m'I

const inputString = "I'm John";

const reverseTheString = (takeTheString) => {
  const copyOfInput = [...takeTheString];
  const lengthOfInputString = takeTheString.length - 1;

  for (let index = 0; index < takeTheString.length; index++) {
    copyOfInput[index] = takeTheString[lengthOfInputString - index];
  }
  return copyOfInput.join(""); // joint('') removes extra commas from array and convert to string--> n', 'h', 'o', 'J', --> nhoJ
};

console.log(reverseTheString(inputString));

// Another way --> with built in function

const reverseTheString2 = (takeTheString) => {
  return takeTheString.split("").reverse().join(""); // split converts to array and reverse the array and join at the end
};

console.log(reverseTheString2(inputString));
