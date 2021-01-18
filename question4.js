// Given two sorted arrays and merge the big one that will also be sorted

// ---> Inputs:  [0, 3, 4, 31], [4, 6, 30]
// Output: [0, 3, 4, 6, 30, 31]

const mergeInputs = (arr1, arr2) => {
  const mergedArray = arr1.concat(arr2);

  for (let i = 0; i < mergedArray.length; i++) {
    let minIndex = i;

    for (let j = i + 1; j < mergedArray.length; j++) {
      if (mergedArray[j] < mergedArray[minIndex]) {
        minIndex = j;
      }
    }

    let temp = mergedArray[minIndex];
    mergedArray[minIndex] = mergedArray[i];
    mergedArray[i] = temp;
  }
  return mergedArray;
  //   console.log(sortedArray);
};

const arr1 = [0, 3, 4, 31];
const arr2 = [4, 6, 30];

console.log(mergeInputs(arr1, arr2));
