// Collection of numbers are given --> find a matching pair that is equal to a given number
// [1, 2, 3, 9] == sum is 8
// [1, 2, 4, 4] == sum is 8
// These arrays are in ascending orders
// Some element may appears twice but we can't add same(index) element.
// All the numbers are integer

// source: https://www.youtube.com/watch?v=XKu_SEDAykw

// The worst solution

const findMatchingPairSum = (collection, givenSum) => {
  for (let index = 0; index < collection.length; index++) {
    for (let item = 0; item < collection.length; item++) {
      if (collection[index] + collection[item] === givenSum) {
        return true;
      }
    }
  }
  return false;
};

const numberCollection = [1, 2, 3, 9];
const numberCollection1 = [1, 2, 4, 4];
const givenSum = 8;

// console.log(findMatchingPairSum(numberCollection1, 8));
// findMatchingPairSum(numberCollection1, givenSum);

// Time complexity 0(n^2) --> Space Complexity is O(1);

// Onternative way

const findMatchingPairSum1 = (collection, givenSum) => {
  collection.some((item) =>
    collection.some((element) => {
      if (item + element === givenSum) {
        console.log("Found");
      }
    })
  );
};

// console.log(findMatchingPairSum1(numberCollection1, 8));

// Time complexity 0(n^2) --> Space Complexity is O(1)

// Alternative way

const findMatchingPairSum2 = (collection, givenSum) => {
  let collectionLength = collection.length;
  let newI = 0;
  for (let i = 0; i < collectionLength; i++) {
    let condition = collection[newI] + collection[collectionLength - 1];
    if (condition === givenSum) {
      return true;
      collectionLength--;
    } else if (condition > givenSum) {
      collectionLength--;
      newI = i;
    } else if (condition < givenSum) {
      newI++;
      continue;
    }
  }
  return false;
};

console.log(findMatchingPairSum2(numberCollection, 8));

// Though its not the best way, but time complexity is 0(n) but space complexity is O(1).
