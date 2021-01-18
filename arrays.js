const strings = ["a", "b", "c", "d"];

// Add at the begining at front O(1)
strings.unshift("o");

// Add element at the middle // O(n) --> because here splice loops through the array.
// We also can delete by the below code
strings.splice(2, 0, "x");

console.log(strings);

// Two types of arrays
// 1. Static Array : Limitation: Fixed in size (When we know the size)

//2. Dynamic Array

// Append can be O(n)
