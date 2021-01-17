// Collection of numbers are given --> find a matching pair that is equal to a given number
// [1, 2, 3, 9] == sum is 8
// [1, 2, 4, 4] == sum is 8
// These arrays are in ascending orders
// Some element may appears twice but we can't add same(index) element.
// All the numbers are integer

// The worst solution

const findMatchingPairSum = (collection, givenSum) => {
  for (let index = 0; index < collection.length; index++) {
    for (let item = 0; item < collection.length; item++) {
      if (collection[index] + collection[item] === givenSum) {
        console.log(collection[index], collection[item]);
        console.log("Found!");
        break;
      }
    }
  }
};

const numberCollection = [1, 2, 3, 9];
const numberCollection1 = [1, 2, 4, 4];
const givenSum = 8;

// console.log(findMatchingPairSum(numberCollection1, 8));
findMatchingPairSum(numberCollection1, givenSum);

// Onternative way
