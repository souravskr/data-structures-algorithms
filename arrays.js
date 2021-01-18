const strings = ["a", "b", "c", "d"];

// Add at the begining at front O(n)
strings.unshift("o");

// Add element at the middle // O(n) --> because here splice loops through the array.
// We also can delete by the below code
strings.splice(2, 0, "x");

// console.log(strings);

// Two types of arrays
// 1. Static Array : Limitation: Fixed in size (When we know the size)

//2. Dynamic Array

// Append can be O(n)

// Build an array from Scratch

// How to build and how to use??

class Array {
  constructor() {
    this.length = 0;
    this.data = {};
  }

  get(index) {
    return this.data[index];
  }

  push(newData) {
    this.data[this.length] = newData;
    this.length++;
  }

  pop() {
    const lastItem = this.length - 1;
    delete this.data[lastItem];
    this.length--;
  }

  unshift(newData) {
    let myData = Object.assign({}, this.data);
    for (let i = 1; i <= this.length; i++) {
      this.data[i] = myData[i - 1];
    }
    this.data[0] = newData;
    this.length++;
  }
}

const myArray = new Array();
myArray.push(1);
myArray.push(2);
myArray.push(3);
myArray.push(4);
myArray.push(5);
myArray.unshift(0);
console.log(myArray);

// String -->

let aString = "Hello";

for (const letter of aString) {
  if (letter === "H") {
    console.log("Found it!");
    break;
  }
}
